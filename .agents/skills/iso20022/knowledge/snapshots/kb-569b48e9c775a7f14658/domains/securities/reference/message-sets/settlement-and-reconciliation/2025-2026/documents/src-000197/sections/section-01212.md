---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.18 Party Identification", "35.1.18.6 PartyIdentificationAndAccount196", "35.1.18.6.4 SafekeepingAccount <SfkpgAcct>"]
file_pages: [1669]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.18.6.4 SafekeepingAccount <SfkpgAcct>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1669 to 1669.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1669

```text
35.1.18.6.4  SafekeepingAccount <SfkpgAcct>
Presence: [0..1]
Definition: Account to or from which a securities entry is made.
SafekeepingAccount <SfkpgAcct> contains the following elements (see "SecuritiesAccount19" on
page 1340 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1341
   Type <Tp> [0..1] ± 1341
   Name <Nm> [0..1] Text 1341
35.1.18.6.5  BlockChainAddressOrWallet <BlckChainAdrOrWllt>
Presence: [0..1]
Definition: Blockchain address or wallet where digital assets are maintained. This is the equivalent of
safekeeping account for digital assets.
BlockChainAddressOrWallet <BlckChainAdrOrWllt> contains the following elements (see
"BlockChainAddressWallet3" on page 1572 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1572
   Type <Tp> [0..1] ± 1572
   Name <Nm> [0..1] Text 1572
35.1.18.6.6  ProcessingDate <PrcgDt>
Presence: [0..1]
Definition: Date/time at which the instruction was processed by the specified party.
ProcessingDate <PrcgDt> contains one of the following elements (see "DateAndDateTime2Choice"
on page 1441 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 1441
Or}   DateTime <DtTm> [1..1] DateTime 1441
35.1.18.6.7  ProcessingIdentification <PrcgId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction for the party identified.
Datatype: "Max35Text" on page 2192
35.1.18.6.8  AdditionalInformation <AddtlInf>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1669 March 2026
```

