---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["8 seev.036.001.17 CorporateActionMovementConfirmationV17", "8.4 Message Building Blocks", "8.4.10 AccountDetails <AcctDtls>", "8.4.10.5 Balance <Bal>", "8.4.10.5.1 ConfirmedBalance <ConfdBal>"]
file_pages: [567]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.036.001.17"]
---

# 8.4.10.5.1 ConfirmedBalance <ConfdBal>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 567 to 567.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 567

```text
Balance <Bal> contains the following CorporateActionBalanceDetails41 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ConfirmedBalance <ConfdBal> [1..1] ± 567
   TotalEligibleBalance <TtlElgblBal> [0..1] ± 568
   BlockedBalance <BlckdBal> [0..1] ± 568
   BorrowedBalance <BrrwdBal> [0..1] ± 568
   CollateralInBalance <CollInBal> [0..1] ± 568
   CollateralOutBalance <CollOutBal> [0..1] ± 569
   OnLoanBalance <OnLnBal> [0..1] ± 569
   PendingDeliveryBalance <PdgDlvryBal> [0..*] ± 569
   PendingReceiptBalance <PdgRctBal> [0..*] ± 570
   OutForRegistrationBalance <OutForRegnBal> [0..1] ± 570
   SettlementPositionBalance <SttlmPosBal> [0..*] ± 570
   StreetPositionBalance <StrtPosBal> [0..1] ± 571
   TradeDatePositionBalance <TradDtPosBal> [0..1] ± 571
   InTransshipmentBalance <InTrnsShipmntBal> [0..1] ± 571
   RegisteredBalance <RegdBal> [0..1] ± 572
   AffectedBalance <AfctdBal> [0..1] ± 572
   UnaffectedBalance <UafctdBal> [0..1] ± 572
Constraints
• AffectedAndUnaffectedBalanceRule
Unaffected balance and Affected balances should only be mentioned as a result of the process that
was run through the event. For instance lottery results, Dutch auction results or tender offer results.
8.4.10.5.1  ConfirmedBalance <ConfdBal>
Presence: [1..1]
Definition: Balance to which the payment applies (less or equal to the total eligible balance).
ConfirmedBalance <ConfdBal> contains one of the following elements (see
"BalanceFormat11Choice" on page 833 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Balance <Bal> [1..1] ± 834
Or   EligibleBalance <ElgblBal> [1..1] ± 834
Or}   NotEligibleBalance <NotElgblBal> [1..1] ± 834
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 567 February 2026
```

