PDF_PATH := .
MEDIA_OUTPUT := media
DOCUMENT_FNAME := presentation
IMAGE_PATH := images
THEME_FILES := beamerthemeNortheastern.sty

DOCUMENT_SUBDIRS :=

# Compiling external images (*.tex) individually is generally more manageable than including with standalone
MEDIA_SOURCES :=

DOCUMENT_SOURCE := $(wildcard *.tex) $(foreach subdir,$(DOCUMENT_SUBDIRS),$(wildcard $(subdir)/*.tex))

# Compile *.tex that are included as graphics
MEDIA_COMPILE_FILES := $(patsubst %.tex,$(MEDIA_OUTPUT)/%.pdf,$(notdir $(MEDIA_SOURCES)))
MEDIA_OUTPUT_FILES := $(MEDIA_COMPILE_FILES)

all: $(PDF_PATH)/$(DOCUMENT_FNAME).pdf

$(MEDIA_OUTPUT):
	mkdir -p $@

$(PDF_PATH)/$(DOCUMENT_FNAME).pdf: $(MEDIA_OUTPUT) $(MEDIA_OUTPUT_FILES) $(DOCUMENT_SOURCE) $(THEME_FILES)
	latexmk -pdf $(DOCUMENT_FNAME)

define media_from_src =
$(patsubst %.tex,$$(MEDIA_OUTPUT)/%.pdf,$(notdir $(1))): $(1)
	cd $(dir $(1)) && pdflatex -output-directory=$$(shell pwd)/$$(MEDIA_OUTPUT) $(notdir $(1))
endef

# generate targets
$(foreach file,$(MEDIA_SOURCES),$(eval $(call media_from_src,$(file))))

clean:
	latexmk -C
	rm -rf $(PDF_PATH)/$(DOCUMENT_FNAME).pdf
	rm -rf $(PDF_PATH)/$(DOCUMENT_FNAME).nav $(PDF_PATH)/$(DOCUMENT_FNAME).listing $(PDF_PATH)/$(DOCUMENT_FNAME).snm $(PDF_PATH)/$(DOCUMENT_FNAME).vrb

cleanall:
	latexmk -CA
	rm -rf $(MEDIA_OUTPUT_FILES) _minted*

.PHONY: clean cleanall
