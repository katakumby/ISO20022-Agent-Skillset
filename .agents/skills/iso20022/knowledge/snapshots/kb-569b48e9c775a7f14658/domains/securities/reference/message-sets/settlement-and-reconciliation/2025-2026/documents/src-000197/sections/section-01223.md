---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.18 Party Identification", "35.1.18.11 PartyIdentificationAndAccount199", "35.1.18.11.6 ProcessingDate <PrcgDt>"]
file_pages: [1680]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.18.11.6 ProcessingDate <PrcgDt>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1680 to 1680.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1680

```text
BlockChainAddressOrWallet <BlckChainAdrOrWllt> contains the following elements (see
"BlockChainAddressWallet3" on page 1572 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1572
   Type <Tp> [0..1] ± 1572
   Name <Nm> [0..1] Text 1572
35.1.18.11.6  ProcessingDate <PrcgDt>
Presence: [0..1]
Definition: Date/time at which the instruction was processed by the specified party.
ProcessingDate <PrcgDt> contains one of the following elements (see "DateAndDateTime2Choice"
on page 1441 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 1441
Or}   DateTime <DtTm> [1..1] DateTime 1441
35.1.18.11.7  ProcessingIdentification <PrcgId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction for the party identified.
Datatype: "Max35Text" on page 2192
35.1.18.11.8  AdditionalInformation <AddtlInf>
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
Settlement And Reconciliation - Maintenance 2025 - 2026 1680 March 2026
```

