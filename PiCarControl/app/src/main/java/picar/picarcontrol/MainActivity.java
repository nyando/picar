package picar.picarcontrol;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.View;
import android.view.Menu;
import android.view.MenuItem;

public class MainActivity extends AppCompatActivity implements View.OnClickListener {

    private static final int FORWARD = 1;
    private static final int BACK    = 2;
    private static final int LEFT    = 3;
    private static final int RIGHT   = 4;
    private static final int CIRCLE  = 5;
    private static final int EXIT    = 6;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Toolbar toolbar = findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        findViewById(R.id.fab).setOnClickListener(this);

        findViewById(R.id.forward).setOnClickListener(this);
        findViewById(R.id.back).setOnClickListener(this);
        findViewById(R.id.left).setOnClickListener(this);
        findViewById(R.id.right).setOnClickListener(this);
        findViewById(R.id.circle).setOnClickListener(this);
        findViewById(R.id.exit).setOnClickListener(this);
    }

    @Override
    public void onClick(View view) {

        switch (view.getId()) {
            case R.id.forward:
                new ControlAsyncTask().execute(FORWARD);
                break;
            case R.id.back:
                new ControlAsyncTask().execute(BACK);
                break;
            case R.id.left:
                new ControlAsyncTask().execute(LEFT);
                break;
            case R.id.right:
                new ControlAsyncTask().execute(RIGHT);
                break;
            case R.id.circle:
                new ControlAsyncTask().execute(CIRCLE);
                break;
            case R.id.exit:
                new ControlAsyncTask().execute(EXIT);
                break;
        }
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }
}
