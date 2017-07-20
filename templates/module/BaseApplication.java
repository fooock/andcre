package %s;

import android.app.Application;

/**
 * Base application class
 */
public abstract class %s extends Application {

    @Override
    public void onCreate() {
        super.onCreate();
        initialize();
    }

   /**
    *
    */
    abstract void initialize();
}