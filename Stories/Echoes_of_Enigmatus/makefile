TEMPLATE_SCRIPT = template.py

.PHONY: all


all: create_structure

create-structure:
ifndef DIR
	$(error DIR is not set. Specify the directory name)
endif 
	mkdir -p $(DIR)
	touch $(DIR)/part1.txt $(DIR)/part1-test.txt
	touch $(DIR)/part2.txt $(DIR)/part2-test.txt
	touch $(DIR)/part3.txt $(DIR)/part3-test.txt
	cp $(TEMPLATE_SCRIPT) $(DIR)/$(DIR).py


