first_arg = "api_key=$(api_key)"
second_arg = "city=$(city)"

.PHONY: build run

build: ;

run:
	 @python client.py $(first_arg) $(second_arg) || true
