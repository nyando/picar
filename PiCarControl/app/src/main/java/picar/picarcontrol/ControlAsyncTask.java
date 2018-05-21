package picar.picarcontrol;

import android.os.AsyncTask;

import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;

public class ControlAsyncTask extends AsyncTask<Integer, Void, Void> {

    private static final String HOSTNAME = "raspberrypi";
    private static final int PORT_NUMBER = 8888;

    @Override
    protected Void doInBackground(Integer... params) {
        try {
            Socket socket = new Socket(HOSTNAME, PORT_NUMBER);
            DataOutputStream out = new DataOutputStream(socket.getOutputStream());
            out.writeInt(params[0]);
            socket.close();
        } catch (IOException ex) {
            ex.printStackTrace();
        }

        return null;
    }
}
