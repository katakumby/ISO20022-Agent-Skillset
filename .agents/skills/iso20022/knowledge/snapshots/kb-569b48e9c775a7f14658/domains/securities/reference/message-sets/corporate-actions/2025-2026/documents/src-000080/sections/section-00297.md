---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.11 AccountDetails <AcctDtls>", "7.4.11.2 AccountsListAndBalanceDetails <AcctsListAndBalDtls>", "7.4.11.2.5 Balance <Bal>", "7.4.11.2.5.1 TotalEligibleBalance <TtlElgblBal>"]
file_pages: [408]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.11.2.5.1 TotalEligibleBalance <TtlElgblBal>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 408 to 408.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 408

```text
Balance <Bal> contains the following CorporateActionBalanceDetails43 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TotalEligibleBalance <TtlElgblBal> [0..1] ± 408
   BlockedBalance <BlckdBal> [0..1] ± 409
   BorrowedBalance <BrrwdBal> [0..1] ± 409
   CollateralInBalance <CollInBal> [0..1] ± 409
   CollateralOutBalance <CollOutBal> [0..1] ± 410
   OnLoanBalance <OnLnBal> [0..1] ± 410
   PendingDeliveryBalance <PdgDlvryBal> [0..*] ± 410
   PendingReceiptBalance <PdgRctBal> [0..*] ± 411
   OutForRegistrationBalance <OutForRegnBal> [0..1] ± 411
   SettlementPositionBalance <SttlmPosBal> [0..*] ± 411
   StreetPositionBalance <StrtPosBal> [0..1] ± 412
   TradeDatePositionBalance <TradDtPosBal> [0..1] ± 412
   InTransshipmentBalance <InTrnsShipmntBal> [0..1] ± 412
   RegisteredBalance <RegdBal> [0..1] ± 413
   ObligatedBalance <OblgtdBal> [0..1] ± 413
   UninstructedBalance <UinstdBal> [0..1] ± 413
   InstructedBalance <InstdBal> [0..1] ± 414
   AffectedBalance <AfctdBal> [0..1] ± 414
   UnaffectedBalance <UafctdBal> [0..1] ± 414
Constraints
• AffectedAndUnaffectedBalanceRule
UnaffectedBalance and AffectedBalance should only be mentioned as a result of the process that
was run through the event. For instance lottery results, Dutch auction results or tender offer results.
7.4.11.2.5.1  TotalEligibleBalance <TtlElgblBal>
Presence: [0..1]
Definition: Total balance of securities eligible for this corporate action event. The entitlement calculation
is based on this balance.
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 408 February 2026
```

