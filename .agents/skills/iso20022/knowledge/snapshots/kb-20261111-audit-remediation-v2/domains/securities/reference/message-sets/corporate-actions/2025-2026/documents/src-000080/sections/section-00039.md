---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.8 AccountDetails <AcctDtls>", "3.4.8.2 AccountsListAndBalanceDetails <AcctsListAndBalDtls>", "3.4.8.2.5 Balance <Bal>", "3.4.8.2.5.1 TotalEligibleBalance <TtlElgblBal>"]
file_pages: [80]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.8.2.5.1 TotalEligibleBalance <TtlElgblBal>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 80 to 80.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 80

```text
Balance <Bal> contains the following CorporateActionBalanceDetails43 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TotalEligibleBalance <TtlElgblBal> [0..1] ± 80
   BlockedBalance <BlckdBal> [0..1] ± 81
   BorrowedBalance <BrrwdBal> [0..1] ± 81
   CollateralInBalance <CollInBal> [0..1] ± 81
   CollateralOutBalance <CollOutBal> [0..1] ± 82
   OnLoanBalance <OnLnBal> [0..1] ± 82
   PendingDeliveryBalance <PdgDlvryBal> [0..*] ± 82
   PendingReceiptBalance <PdgRctBal> [0..*] ± 83
   OutForRegistrationBalance <OutForRegnBal> [0..1] ± 83
   SettlementPositionBalance <SttlmPosBal> [0..*] ± 83
   StreetPositionBalance <StrtPosBal> [0..1] ± 84
   TradeDatePositionBalance <TradDtPosBal> [0..1] ± 84
   InTransshipmentBalance <InTrnsShipmntBal> [0..1] ± 84
   RegisteredBalance <RegdBal> [0..1] ± 85
   ObligatedBalance <OblgtdBal> [0..1] ± 85
   UninstructedBalance <UinstdBal> [0..1] ± 85
   InstructedBalance <InstdBal> [0..1] ± 86
   AffectedBalance <AfctdBal> [0..1] ± 86
   UnaffectedBalance <UafctdBal> [0..1] ± 86
Constraints
• AffectedAndUnaffectedBalanceRule
UnaffectedBalance and AffectedBalance should only be mentioned as a result of the process that
was run through the event. For instance lottery results, Dutch auction results or tender offer results.
3.4.8.2.5.1  TotalEligibleBalance <TtlElgblBal>
Presence: [0..1]
Definition: Total balance of securities eligible for this corporate action event. The entitlement calculation
is based on this balance.
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 80 February 2026
```

