---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["2 camt.003.001.08 GetAccountV08", "2.4 Message Building Blocks", "2.4.2 AccountQueryDefinition <AcctQryDef>", "2.4.2.2 AccountCriteria <AcctCrit>", "2.4.2.2.2 NewCriteria <NewCrit>", "2.4.2.2.2.2 SearchCriteria <SchCrit>", "2.4.2.2.2.2.1 AccountIdentification <AcctId>", "2.4.2.2.2.2.1.2 ContainText <CTTxt>"]
file_pages: [30, 31]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.003.001.08"]
---

# 2.4.2.2.2.2.1.2 ContainText <CTTxt>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 30 to 31.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 30

```text
2.4.2.2.2.2.1.2  ContainText <CTTxt>
Presence: [1..1]
Definition: Search for one or more accounts based on partial identification of the account(s).
Datatype: "Max35Text" on page 889
2.4.2.2.2.2.1.3  NotContainText <NCTTxt>
Presence: [1..1]
Definition: Search for one or more accounts based on a pattern that cannot be contained in the account
identification.
Datatype: "Max35Text" on page 889
2.4.2.2.2.2.2  Type <Tp>
Presence: [0..*]
Definition: Specifies the nature, or use, of the cash account.
Type <Tp> contains one of the following elements (see "CashAccountType2Choice" on page 786 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 786
Or}   Proprietary <Prtry> [1..1] Text 786
2.4.2.2.2.2.3  Currency <Ccy>
Presence: [0..*]
Definition: Specifies the currency of the cash account.
Impacted by: C1 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 849
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
2.4.2.2.2.2.4  Balance <Bal>
Presence: [0..*]
Definition: Balance of the account which is being queried.
Impacted by: C5 "CounterpartyIdentification1Rule", C6 "CounterpartyIdentification2Rule"
Approved by the Payments SEG on 04 February 2025 camt.003.001.08 GetAccountV08
Cash Management - Maintenance 2024 - 2025 30 February 2025
```

## File page 31

```text
Balance <Bal> contains the following CashBalance14 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..*]  32
{Or     Code <Cd> [1..1] CodeSet 32
Or}     Proprietary <Prtry> [1..1] Text 32
   CounterpartyType <CtrPtyTp> [1..1] CodeSet 32
   CounterpartyIdentification <CtrPtyId> [0..*] ± 33
   ValueDate <ValDt> [0..*]  33
{Or     DateTime <DtTm> [1..1]  34
{Or       FromDateTime <FrDtTm> [1..1] DateTime 34
Or       ToDateTime <ToDtTm> [1..1] DateTime 34
Or       FromToDateTime <FrToDtTm> [1..1] ± 35
Or       EqualDateTime <EQDtTm> [1..1] DateTime 35
Or}       NotEqualDateTime <NEQDtTm> [1..1] DateTime 35
Or}     Date <Dt> [1..1]  35
{Or       FromDate <FrDt> [1..1] Date 35
Or       ToDate <ToDt> [1..1] Date 35
Or       FromToDate <FrToDt> [1..1] ± 36
Or       EqualDate <EQDt> [1..1] Date 36
Or}       NotEqualDate <NEQDt> [1..1] Date 36
   ProcessingDate <PrcgDt> [0..1]  36
{Or     DateTime <DtTm> [1..1]  37
{Or       FromDateTime <FrDtTm> [1..1] DateTime 37
Or       ToDateTime <ToDtTm> [1..1] DateTime 37
Or       FromToDateTime <FrToDtTm> [1..1] ± 38
Or       EqualDateTime <EQDtTm> [1..1] DateTime 38
Or}       NotEqualDateTime <NEQDtTm> [1..1] DateTime 38
Or}     Date <Dt> [1..1]  38
{Or       FromDate <FrDt> [1..1] Date 38
Or       ToDate <ToDt> [1..1] Date 38
Or       FromToDate <FrToDt> [1..1] ± 39
Or       EqualDate <EQDt> [1..1] Date 39
Or}       NotEqualDate <NEQDt> [1..1] Date 39
Approved by the Payments SEG on 04 February 2025 camt.003.001.08 GetAccountV08
Cash Management - Maintenance 2024 - 2025 31 February 2025
```

