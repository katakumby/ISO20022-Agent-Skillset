---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["5 seev.033.001.14 CorporateActionInstructionV14", "5.4 Message Building Blocks", "5.4.7 AccountDetails <AcctDtls>", "5.4.7.5 Balance <Bal>", "5.4.7.5.10 SettlementPositionBalance <SttlmPosBal>"]
file_pages: [299]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.033.001.14"]
---

# 5.4.7.5.10 SettlementPositionBalance <SttlmPosBal>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 299 to 299.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 299

```text
OutForRegistrationBalance <OutForRegnBal> contains one of the following elements (see
"BalanceFormat11Choice" on page 833 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Balance <Bal> [1..1] ± 834
Or   EligibleBalance <ElgblBal> [1..1] ± 834
Or}   NotEligibleBalance <NotElgblBal> [1..1] ± 834
5.4.7.5.10  SettlementPositionBalance <SttlmPosBal>
Presence: [0..1]
Definition: Balance of securities representing only settled transactions; pending transactions not
included.
SettlementPositionBalance <SttlmPosBal> contains one of the following elements (see
"BalanceFormat11Choice" on page 833 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Balance <Bal> [1..1] ± 834
Or   EligibleBalance <ElgblBal> [1..1] ± 834
Or}   NotEligibleBalance <NotElgblBal> [1..1] ± 834
5.4.7.5.11  StreetPositionBalance <StrtPosBal>
Presence: [0..1]
Definition: Balance of financial instruments that remain registered in the name of the prior beneficial
owner.
StreetPositionBalance <StrtPosBal> contains one of the following elements (see
"BalanceFormat11Choice" on page 833 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Balance <Bal> [1..1] ± 834
Or   EligibleBalance <ElgblBal> [1..1] ± 834
Or}   NotEligibleBalance <NotElgblBal> [1..1] ± 834
5.4.7.5.12  TradeDatePositionBalance <TradDtPosBal>
Presence: [0..1]
Definition: Balance of securities based on trade date, for example, includes all pending transactions in
addition to the balance of settled transactions.
Approved by the Securities SEG on 27 January 2026 seev.033.001.14 CorporateActionInstructionV14
Corporate Actions - Maintenance 2025 - 2026 299 February 2026
```

