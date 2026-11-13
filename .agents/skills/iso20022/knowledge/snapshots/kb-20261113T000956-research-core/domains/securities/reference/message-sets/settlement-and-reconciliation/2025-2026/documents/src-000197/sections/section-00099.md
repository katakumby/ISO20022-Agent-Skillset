---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 semt.013.001.07 IntraPositionMovementInstructionV07", "4.4 Message Building Blocks", "4.4.8 SafekeepingPlace <SfkpgPlc>"]
file_pages: [142]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.013.001.07"]
---

# 4.4.8 SafekeepingPlace <SfkpgPlc>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 142 to 142.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 142

```text
BlockChainAddressOrWallet <BlckChainAdrOrWllt> contains the following elements (see
"BlockChainAddressWallet3" on page 1572 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1572
   Type <Tp> [0..1] ± 1572
   Name <Nm> [0..1] Text 1572
4.4.8 SafekeepingPlace <SfkpgPlc>
Presence: [0..1]
Definition: Place where the securities are safe-kept, physically or notionally. This place can be, for
example, a local custodian, a Central Securities Depository (CSD) or an International Central Securities
Depository (ICSD).
SafekeepingPlace <SfkpgPlc> contains one of the following elements (see
"SafekeepingPlaceFormat41Choice" on page 1648 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Identification <Id> [1..1]  1649
     SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 1649
     Identification <Id> [0..1] Text 1649
Or   Country <Ctry> [1..1] CodeSet C7 1649
Or   DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1650
Or   TypeAndIdentification <TpAndId> [1..1]  1650
     SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 1650
     Identification <Id> [1..1] IdentifierSet C5 1650
Or}   Proprietary <Prtry> [1..1] ± 1651
4.4.9 FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
Impacted by: C10 "DescriptionPresenceRule", C11 "DescriptionUsageRule", C13 "ISINGuideline", C14
"ISINPresenceRule", C15 "OtherIdentificationPresenceRule"
Approved by the Securities SEG on 27 January 2026 semt.013.001.07
IntraPositionMovementInstructionV07
Settlement And Reconciliation - Maintenance 2025 - 2026 142 March 2026
```

