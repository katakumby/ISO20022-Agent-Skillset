---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.18 Party Identification", "35.1.18.25 PartyIdentification315", "35.1.18.25.4 ProcessingDate <PrcgDt>"]
file_pages: [1703]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.18.25.4 ProcessingDate <PrcgDt>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1703 to 1703.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1703

```text
AlternateIdentification <AltrnId> contains the following elements (see "AlternatePartyIdentification7"
on page 1691 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   IdentificationType <IdTp> [1..1] ± 1691
   Country <Ctry> [1..1] CodeSet C7 1691
   AlternateIdentification <AltrnId> [1..1] Text 1691
35.1.18.25.4  ProcessingDate <PrcgDt>
Presence: [0..1]
Definition: Date/time at which the instruction was processed by the specified party.
ProcessingDate <PrcgDt> contains one of the following elements (see "DateAndDateTime2Choice"
on page 1441 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 1441
Or}   DateTime <DtTm> [1..1] DateTime 1441
35.1.18.25.5  ProcessingIdentification <PrcgId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction for the party identified.
Datatype: "Max35Text" on page 2192
35.1.18.25.6  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Provides additional information to a party identification.
Impacted by: C5 "AdditonalDetailsGuideline"
AdditionalInformation <AddtlInf> contains the following elements (see "PartyTextInformation1" on
page 1690 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DeclarationDetails <DclrtnDtls> [0..1] Text 1690
   PartyContactDetails <PtyCtctDtls> [0..1] Text 1690
   RegistrationDetails <RegnDtls> [0..1] Text 1691
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1703 March 2026
```

