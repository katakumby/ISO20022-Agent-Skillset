---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["5 seev.033.001.14 CorporateActionInstructionV14", "5.4 Message Building Blocks", "5.4.7 AccountDetails <AcctDtls>", "5.4.7.5 Balance <Bal>"]
file_pages: [295]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.033.001.14"]
---

# 5.4.7.5 Balance <Bal>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 295 to 295.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 295

```text
SafekeepingPlace <SfkpgPlc> contains one of the following elements (see
"SafekeepingPlaceFormat42Choice" on page 1130 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Identification <Id> [1..1]  1130
     SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 1130
     Identification <Id> [0..1] Text 1131
Or   Country <Ctry> [1..1] CodeSet C3 1131
Or   DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1131
Or   TypeAndIdentification <TpAndId> [1..1]  1131
     SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 1132
     Identification <Id> [1..1] IdentifierSet C1 1132
Or}   Proprietary <Prtry> [1..1] ± 1132
5.4.7.5  Balance <Bal>
Presence: [0..1]
Definition: Provides information about balance related to a corporate action.
Balance <Bal> contains the following CorporateActionBalanceDetails42 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TotalEligibleBalance <TtlElgblBal> [0..1] ± 296
   BlockedBalance <BlckdBal> [0..1] ± 296
   BorrowedBalance <BrrwdBal> [0..1] ± 296
   CollateralInBalance <CollInBal> [0..1] ± 297
   CollateralOutBalance <CollOutBal> [0..1] ± 297
   OnLoanBalance <OnLnBal> [0..1] ± 297
   PendingDeliveryBalance <PdgDlvryBal> [0..*] ± 298
   PendingReceiptBalance <PdgRctBal> [0..*] ± 298
   OutForRegistrationBalance <OutForRegnBal> [0..1] ± 298
   SettlementPositionBalance <SttlmPosBal> [0..1] ± 299
   StreetPositionBalance <StrtPosBal> [0..1] ± 299
   TradeDatePositionBalance <TradDtPosBal> [0..1] ± 299
   InTransshipmentBalance <InTrnsShipmntBal> [0..1] ± 300
   RegisteredBalance <RegdBal> [0..1] ± 300
Approved by the Securities SEG on 27 January 2026 seev.033.001.14 CorporateActionInstructionV14
Corporate Actions - Maintenance 2025 - 2026 295 February 2026
```

