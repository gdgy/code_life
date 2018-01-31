# include <stdio.h>
#include <event.h> 
#include <event2/event.h>
void run_base_with_ticks(struct event_base *base)
{
    struct timeval ten_sec;
    ten_sec.tv_sec = 3;
    ten_sec.tv_usec = 0;
    
    while (1) {
        /* This schedules an exit ten seconds from now. */
        event_base_loopexit(base, &ten_sec);
        event_base_dispatch(base);
        printf("exit:%d break:%d \n", event_base_got_exit(base), event_base_got_break(base));
        puts("Tick");
    }
}

int main()
{
    int i;
    const char **methods = event_get_supported_methods();
    printf("Starting Libevent %s. Available methods are:\n",
    event_get_version());
    for (i=0; methods[i] != NULL; ++i)
    {
        printf(" %s\n", methods[i]);
    }
    
    struct event_base *base;
    enum event_method_feature f;
    base = event_base_new();
    if (!base) {
        puts("Couldn't get an event_base!");
    } else {
        printf("Using Libevent with backend method %s.",event_base_get_method(base));
        f = event_base_get_features(base);
        if ((f & EV_FEATURE_ET))
        printf(" Edge-triggered events are supported.");
        if ((f & EV_FEATURE_O1))
        printf(" O(1) event notification is supported.");
        if ((f & EV_FEATURE_FDS))
        printf("All FD types are supported.");
        puts("");
    }
    run_base_with_ticks(base);
    
    
}