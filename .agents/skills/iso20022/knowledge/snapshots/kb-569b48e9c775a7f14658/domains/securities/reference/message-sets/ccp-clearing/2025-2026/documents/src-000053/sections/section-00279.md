---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["11 MX secl.010.001.04 SettlementObligationReportV04", "11.4 Message Building Blocks", "11.4.7 SettlementParties <SttlmPties>", "11.4.7.1 DeliveringSettlementParties <DlvrgSttlmPties>"]
file_pages: [368]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.010.001.04"]
---

# 11.4.7.1 DeliveringSettlementParties <DlvrgSttlmPties>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 368 to 368.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 368

```text
SettlementParties <SttlmPties> contains one of the following SettlementParties37Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   DeliveringSettlementParties <DlvrgSttlmPties> [0..1]  C10 368
     Depository <Dpstry> [1..1] ± 369
     Party1 <Pty1> [1..1] ± 369
     Party2 <Pty2> [0..1] ± 369
     SecuritiesSettlementSystem <SctiesSttlmSys> [0..1] Text 370
Or}   ReceivingSettlementParties <RcvgSttlmPties> [0..1]  C11 370
     Depository <Dpstry> [1..1] ± 371
     Party1 <Pty1> [1..1] ± 371
     Party2 <Pty2> [0..1] ± 371
     SecuritiesSettlementSystem <SctiesSttlmSys> [0..1] Text 372
11.4.7.1  DeliveringSettlementParties <DlvrgSttlmPties>
Presence: [0..1]
Definition: Chain of parties involved in the settlement of a transaction, including receipts and deliveries,
book transfers, treasury deals, or other activities, resulting in the movement of a security or amount of
money from one account to another.
Impacted by: C10 DepositoryGuideline
DeliveringSettlementParties <DlvrgSttlmPties> contains the following
DeliveringPartiesAndAccount21 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Depository <Dpstry> [1..1] ± 369
   Party1 <Pty1> [1..1] ± 369
   Party2 <Pty2> [0..1] ± 369
   SecuritiesSettlementSystem <SctiesSttlmSys> [0..1] Text 370
Constraints
• DepositoryGuideline
(Rule)
In a receive, the delivering depository is to be understood as the requested depository of the
delivering counterparty.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.010.001.04 SettlementObligationReportV04
March 2026 368
```

