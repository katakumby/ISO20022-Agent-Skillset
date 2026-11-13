---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.15 Entry <Ntry>", "2.4.2.15.18 EntryDetails <NtryDtls>", "2.4.2.15.18.2 TransactionDetails <TxDtls>", "2.4.2.15.18.2.16 RelatedDates <RltdDts>", "2.4.2.15.18.2.16.1 AcceptanceDateTime <AccptncDtTm>"]
file_pages: [208]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.15.18.2.16.1 AcceptanceDateTime <AccptncDtTm>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 208 to 208.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 208

```text
RelatedDates <RltdDts> contains the following TransactionDates3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AcceptanceDateTime <AccptncDtTm> [0..1] DateTime 208
   TradeActivityContractualSettlementDate
<TradActvtyCtrctlSttlmDt>
[0..1] Date 208
   TradeDate <TradDt> [0..1] Date 208
   InterbankSettlementDate <IntrBkSttlmDt> [0..1] Date 208
   StartDate <StartDt> [0..1] Date 208
   EndDate <EndDt> [0..1] Date 209
   TransactionDateTime <TxDtTm> [0..1] DateTime 209
   Proprietary <Prtry> [0..*]  209
     Type <Tp> [1..1] Text 209
     Date <Dt> [1..1] ± 209
2.4.2.15.18.2.16.1  AcceptanceDateTime <AccptncDtTm>
Presence: [0..1]
Definition: Point in time when the payment order from the initiating party meets the processing
conditions of the account servicing agent. This means that the account servicing agent has received the
payment order and has applied checks such as authorisation, availability of funds.
Datatype: "ISODateTime" on page 908
2.4.2.15.18.2.16.2  TradeActivityContractualSettlementDate <TradActvtyCtrctlSttlmDt>
Presence: [0..1]
Definition: Identifies when an amount of money should have contractually been credited or debited the
account versus when the amount of money was actually settled (debited/credited) on the cash account.
Datatype: "ISODate" on page 908
2.4.2.15.18.2.16.3  TradeDate <TradDt>
Presence: [0..1]
Definition: Date on which the trade was executed.
Datatype: "ISODate" on page 908
2.4.2.15.18.2.16.4  InterbankSettlementDate <IntrBkSttlmDt>
Presence: [0..1]
Definition: Date on which the amount of money ceases to be available to the agent that owes it and
when the amount of money becomes available to the agent to which it is due.
Datatype: "ISODate" on page 908
2.4.2.15.18.2.16.5  StartDate <StartDt>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
208 March 2026
```

