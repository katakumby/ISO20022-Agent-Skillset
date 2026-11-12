---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.60 CorporateActionNarrative3Choice"]
file_pages: [983]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.60 CorporateActionNarrative3Choice

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 983 to 983.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 983

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
16.1.15.60  CorporateActionNarrative3Choice
Definition: Choice between a standard code or a proprietary code to specify the narrative type of
corporate action.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 983
Or}   Proprietary <Prtry> [1..1] ± 983
16.1.15.60.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to specify the narrative type of the message.
Datatype: "CorporateActionNarrative1Code" on page 1195
CodeName Name Definition
TAXE TaxationConditions Provides taxation conditions that cannot
be included within the structured fields of
this message.
REGI RegistrationDetails Provides information required for the
registration.
WTRC WithholdingTaxReliefCertification Certification process for withholding tax
reduction or exemption based on the tax
status of the holder.
RFMC ICSDRefusalOfMarkUpDownConfirmation In the context of a corporate action, an
International Central Securities
Depository (ICSD) refuses a mark-up/
mark-down confirmation sent by the
account servicer.
PAUT ChasingOfPriorAuthorization International Central Securities
Depository (ICSD) chases the
authorisation from the account servicer
in order to process the exchange from
global temporary to global permanent.
CTIN ConfirmationOfHoldingTransfer Confirmation of transfer of interests
between International Central Securities
Depositories (ICSDs) following a
corporate actions.
16.1.15.60.2  Proprietary <Prtry>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 983 February 2026
```

