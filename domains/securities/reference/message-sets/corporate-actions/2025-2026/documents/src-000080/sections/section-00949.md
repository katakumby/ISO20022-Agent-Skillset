---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.2 Message Datatypes", "16.2.2 CodeSet", "16.2.2.24 CorporateActionChangeType2Code"]
file_pages: [1168]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.2.2.24 CorporateActionChangeType2Code

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 1168 to 1168.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1168

```text
16.2.2.24  CorporateActionChangeType2Code
Definition: Specifies the type of changes.
Type: CodeSet
CodeName Name Definition
BERE BearToRegistered Change from bearer into registered form.
CERT Certificates Change of all instruments into
certificates.
DEPH DematerialisedToPhysical Change from dematerialised into
physical form.
GPPH GlobalPermanentToPhysical Change from global permanent to
physical form.
GTGP GlobalTemporaryToGlobalPermanent Change from global temporary to global
permanent form.
GTPH GlobalTemporaryToPhysical Change from global temporary to
physical form.
NAME Name The issuing company changes its name.
CA event shows the change from old
name to new name and may involve
surrendering physical shares with the old
name to the registrar.
PHDE PhysicalToDematerialised Change from physical into
dematerialised form.
REBE RegisteredToBearer Change from registered into bearer form.
TERM Terms Change in the terms of the security.
16.2.2.25  CorporateActionEventProcessingType1Code
Definition: Specifies the type of event processing.
Type: CodeSet
CodeName Name Definition
GENL General No debit or credit of resources.
DISN Distribution Holder of the relevant security on a
certain date, for example, the record
date, will receive a benefit without giving
up the underlying security.
REOR Reorganisation Underlying security will be debited and
may be replaced by another resource (or
resources).
16.2.2.26  CorporateActionEventStage3Code
Definition: Specifies the stage of the CA event.
Type: CodeSet
CodeName Name Definition
APPD Approved Approved at the relevant meeting, for
example, dividend.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1168 February 2026
```

