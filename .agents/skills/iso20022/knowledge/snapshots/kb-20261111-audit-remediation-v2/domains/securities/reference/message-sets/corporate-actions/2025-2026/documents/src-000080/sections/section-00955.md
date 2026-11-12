---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.2 Message Datatypes", "16.2.2 CodeSet", "16.2.2.34 CorporateActionMandatoryVoluntary1Code"]
file_pages: [1195]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.2.2.34 CorporateActionMandatoryVoluntary1Code

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 1195 to 1195.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1195

```text
Type: CodeSet
CodeName Name Definition
CONF ConferenceCall Information is about an informal call
when an issuer, trustee, agent wishes to
talk to note holders to discuss a certain
issue or potential change to the notes;
nothing said being binding.
16.2.2.34  CorporateActionMandatoryVoluntary1Code
Definition: Specifies whether the event is mandatory, mandatory with options or voluntary.
Type: CodeSet
CodeName Name Definition
MAND Mandatory Participation in CA event is mandatory.
Further instructions from the account
owner are not required.
CHOS MandatoryWithOptions Participation in the corporate action is
mandatory and further instructions from
the account owner are required, unless a
default option has been specified.
VOLU Voluntary Participation in the corporate action is
voluntary. If the owner wishes to take
part in the event, instructions from the
account owner are required.
16.2.2.35  CorporateActionMovementPreliminaryAdviceFunction1Code
Definition: Specifies whether the message is a final eligible balance and entitlements message or a
preliminary advice of payment message.
Type: CodeSet
CodeName Name Definition
ENTL Entitlement Message is an entitlement.
CAPA PreadviceOfMovement Message is a preadvice of movement.
16.2.2.36  CorporateActionNarrative1Code
Definition: Specifies the narrative type of a corporate action.
Type: CodeSet
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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1195 February 2026
```

