package %s;

import timber.log.Timber;

/**
 *
 */
public class DefaultApplication extends %s {

    @Override
    void initialize() {
        Timber.plant(new Timber.DebugTree());
    }
}