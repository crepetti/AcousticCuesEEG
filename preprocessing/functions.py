"""Helper functions used by individual_preproc.ipynb."""
import numpy as np
from matplotlib import pyplot as plt


def filter_short_bursts(events, raw, min_amplitude=20000, min_duration=0.75):
    """Remove spurious trigger pulses so that one event remains per stimulus onset.

    1. Drop events whose largest absolute value across channels at the event sample
       is below `min_amplitude`. At that sample the largest value is the trigger
       code on the Status channel (EEG values are in volts, i.e. ~1e-5), so this
       keeps only trigger codes >= `min_amplitude`.
    2. Of events less than `min_duration` seconds apart, keep only the last one.

    Parameters
    ----------
    events : ndarray, shape (n_events, 3)
        Output of mne.find_events.
    raw : mne.io.Raw
        Raw data including the Status (trigger) channel.
    min_amplitude : float
        Minimum trigger-channel value for an event to be kept.
    min_duration : float
        Minimum time (s) between consecutive kept events.

    Returns
    -------
    ndarray, shape (n_kept, 3)
    """
    sfreq = raw.info['sfreq']
    data, _ = raw[:, :]

    # Step 1: keep events whose trigger value reaches min_amplitude
    valid_events = np.array([ev for ev in events
                             if np.max(np.abs(data[:, ev[0]])) >= min_amplitude])

    # Step 2: drop an event if the next one follows within min_duration
    final_events = [ev for i, ev in enumerate(valid_events[:-1])
                    if (valid_events[i + 1][0] - ev[0]) / sfreq >= min_duration]
    if len(valid_events) > 0:
        final_events.append(valid_events[-1])

    return np.array(final_events)


def plot_trigger_data_and_events(trig_data, events, sfreq):
    """Plot the trigger channel (ms on the x axis) with a red dot at each event."""
    time_ms = (np.arange(len(trig_data)) / sfreq) * 1000

    fig, ax = plt.subplots(figsize=[20, 5])
    ax.plot(time_ms, trig_data, color='black')
    for ev in events:
        ax.plot((ev[0] / sfreq) * 1000, trig_data[ev[0]], 'ro')
    ax.set_title(f'N_triggers={len(events)}')
    ax.set_xlabel('Time (ms)')
    ax.set_ylabel('Trigger signal')
    return fig
