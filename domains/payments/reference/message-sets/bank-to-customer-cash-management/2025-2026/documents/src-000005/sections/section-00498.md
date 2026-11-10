---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.14 Entry <Ntry>", "4.4.2.14.18 EntryDetails <NtryDtls>", "4.4.2.14.18.2 TransactionDetails <TxDtls>", "4.4.2.14.18.2.16 RelatedDates <RltdDts>", "4.4.2.14.18.2.16.1 AcceptanceDateTime <AccptncDtTm>"]
file_pages: [726]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.14.18.2.16.1 AcceptanceDateTime <AccptncDtTm>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 726 to 726.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 726

```text
RelatedDates <RltdDts> contains the following TransactionDates3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AcceptanceDateTime <AccptncDtTm> [0..1] DateTime 726
   TradeActivityContractualSettlementDate
<TradActvtyCtrctlSttlmDt>
[0..1] Date 726
   TradeDate <TradDt> [0..1] Date 726
   InterbankSettlementDate <IntrBkSttlmDt> [0..1] Date 726
   StartDate <StartDt> [0..1] Date 726
   EndDate <EndDt> [0..1] Date 727
   TransactionDateTime <TxDtTm> [0..1] DateTime 727
   Proprietary <Prtry> [0..*]  727
     Type <Tp> [1..1] Text 727
     Date <Dt> [1..1] ± 727
4.4.2.14.18.2.16.1  AcceptanceDateTime <AccptncDtTm>
Presence: [0..1]
Definition: Point in time when the payment order from the initiating party meets the processing
conditions of the account servicing agent. This means that the account servicing agent has received the
payment order and has applied checks such as authorisation, availability of funds.
Datatype: "ISODateTime" on page 908
4.4.2.14.18.2.16.2  TradeActivityContractualSettlementDate <TradActvtyCtrctlSttlmDt>
Presence: [0..1]
Definition: Identifies when an amount of money should have contractually been credited or debited the
account versus when the amount of money was actually settled (debited/credited) on the cash account.
Datatype: "ISODate" on page 908
4.4.2.14.18.2.16.3  TradeDate <TradDt>
Presence: [0..1]
Definition: Date on which the trade was executed.
Datatype: "ISODate" on page 908
4.4.2.14.18.2.16.4  InterbankSettlementDate <IntrBkSttlmDt>
Presence: [0..1]
Definition: Date on which the amount of money ceases to be available to the agent that owes it and
when the amount of money becomes available to the agent to which it is due.
Datatype: "ISODate" on page 908
4.4.2.14.18.2.16.5  StartDate <StartDt>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
726 March 2026
```

