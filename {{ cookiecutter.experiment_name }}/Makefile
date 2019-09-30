.PHONY: all clean cleanall force

all: {{ cookiecutter.veins.path }}
ifdef MODE
	@cd src && $(MAKE)
else
	@cd src && $(MAKE) MODE=release
	@cd src && $(MAKE) MODE=debug
endif

{{ cookiecutter.veins.path }}: force
	$(MAKE) -C $@

clean:
	@cd {{ cookiecutter.veins.path }} && $(MAKE) clean

cleanall:
	@cd {{ cookiecutter.veins.path }} && $(MAKE) cleanall
	$(RM) src/Makefile
	$(RM) src/experiment
	$(RM) src/experiment_dbg
	$(RM) out

force:
	@true
