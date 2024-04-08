# This file was created multiple commands for testing.

Dir := $(shell pwd)
Code_dir := $(subst tests/CodeInterpretation,projectCICD/AESClone,$(Dir))
Docker_dir := $(subst tests/CodeInterpretation,docker,$(Dir))
Test_dir := $(subst CodeInterpretation,unit,$(Dir))
Code_name := main.py
Test_code := test_functions.py
Copy_code = $(shell cd $(Code_dir); cp $(Code_name) $(Docker_dir))



# Adding the source code to the docker folder configuration
docker-module: run-main-py test-main-py clean code-to-docker
	@echo "*** updating the docker folder configuration........ 	***"


# Running the main code
run-main-py:
	@echo "\n"
	@echo "***	running the $(Code_name) ......	***\n"
	@ cd $(Code_dir); \
	python3.9 $(Code_name)
	@echo "\n***	the code has successfully ran.......	***\n"

# Running the test
test-main-py:
	@echo "\n"
	@echo "***	testing the $(Test_code) ......	***\n"
	@ cd $(Test_dir); \
	python3.9 $(Test_code)
	@echo "\n***	the test has successfully ran.......	***\n"


# Cleaning previous versions of the source code
clean:
	@cd $(Docker_dir);\
	if [ -f $(Code_name) ]; then \
		rm -f $(Code_name); \
		echo "***	updating the previous version.......	***";\
	else \
		echo "***	Addding to the base code.......		***";\
	fi

# Copying the running source code to docker folders
code-to-docker:
	@echo "\n"
	@echo "***	Copying the code to docker.......	***\n"
	@cd $(Docker_dir);\
	$(Copy_code)
