#include <stdio.h>
#include <dispatch/dispatch.h>

int main()
{
	dispatch_async(dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0), ^{
		printf("Successfully initialized libdispatch.  Hello from a non-main thread.\n");
		_exit(0);
	});

	dispatch_main();
}
