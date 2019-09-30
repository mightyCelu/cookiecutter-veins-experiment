.PHONY: all clean cleanall force

all: {{ cookiecutter.plexe.path }}
ifdef MODE
	@cd src && $(MAKE)
else
	@cd src && $(MAKE) MODE=release
	@cd src && $(MAKE) MODE=debug
endif

{{ cookiecutter.plexe.path }}: {{ cookiecutter.veins.path }} force
	$(MAKE) -C $@

{{ cookiecutter.veins.path }}: force
	$(MAKE) -C $@

clean:
	@cd {{ cookiecutter.veins.path }} && $(MAKE) clean
	@cd {{ cookiecutter.plexe.path }} && $(MAKE) clean

cleanall:
	@cd {{ cookiecutter.veins.path }} && $(MAKE) cleanall
	@cd {{ cookiecutter.plexe.path }} && $(MAKE) cleanall
	$(RM) src/Makefile
	$(RM) src/experiment
	$(RM) src/experiment_dbg
	$(RM) out

force:
	@true
