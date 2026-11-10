---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "T2S Administration"
source_ids: ["src-000344"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["2 admi.005.001.02 ReportQueryRequestV02", "2.4 Message Building Blocks", "2.4.2 ReportQueryCriteria <RptQryCrit>", "2.4.2.2 SearchCriteria <SchCrit>", "2.4.2.2.1 AccountIdentification <AcctId>", "2.4.2.2.1.1 Equal <EQ>"]
file_pages: [13, 14]
content_origin: "source-text-extraction"
mentioned_message_ids: ["admi.005.001.02"]
---

# 2.4.2.2.1.1 Equal <EQ>

Source: [src-000344](../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart2_Target2Securities_Administration_2023_2024_v1.pdf`. Locator: one-based file pages 13 to 14.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 13

```text
2.4.2.2.1.1  Equal <EQ>
Presence: [1..1]
Definition: Search for one or more accounts based on exact identification of the account(s).
Equal <EQ> contains one of the following elements (see "AccountIdentification4Choice" on page 39
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C6 39
Or}   Other <Othr> [1..1] ± 39
2.4.2.2.1.2  ContainText <CTTxt>
Presence: [1..1]
Definition: Search for one or more accounts based on partial identification of the account(s).
Datatype: "Max35Text" on page 69
2.4.2.2.1.3  NotContainText <NCTTxt>
Presence: [1..1]
Definition: Search for one or more accounts based on a pattern that cannot be contained in the account
identification.
Datatype: "Max35Text" on page 69
2.4.2.2.2  Balance <Bal>
Presence: [0..*]
Definition: Numerical representation of the net increases and decreases in an account at a specific
point in time. A cash balance is calculated from a sum of cash credits minus a sum of cash debits.
Impacted by: C3 "CounterpartyIdentification1Rule", C4 "CounterpartyIdentification2Rule"
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
admi.005.001.02 ReportQueryRequestV02
Target2-Securities - Administration - Maintenance 2023 -
2024
13 March 2024
```

## File page 14

```text
Balance <Bal> contains the following CashBalance14 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..*]  15
{Or     Code <Cd> [1..1] CodeSet 15
Or}     Proprietary <Prtry> [1..1] Text 15
   CounterpartyType <CtrPtyTp> [1..1] CodeSet 15
   CounterpartyIdentification <CtrPtyId> [0..*] ± 16
   ValueDate <ValDt> [0..*]  16
{Or     DateTime <DtTm> [1..1]  17
{Or       FromDateTime <FrDtTm> [1..1] DateTime 17
Or       ToDateTime <ToDtTm> [1..1] DateTime 17
Or       FromToDateTime <FrToDtTm> [1..1] ± 18
Or       EqualDateTime <EQDtTm> [1..1] DateTime 18
Or}       NotEqualDateTime <NEQDtTm> [1..1] DateTime 18
Or}     Date <Dt> [1..1]  18
{Or       FromDate <FrDt> [1..1] Date 18
Or       ToDate <ToDt> [1..1] Date 18
Or       FromToDate <FrToDt> [1..1] ± 19
Or       EqualDate <EQDt> [1..1] Date 19
Or}       NotEqualDate <NEQDt> [1..1] Date 19
   ProcessingDate <PrcgDt> [0..1]  19
{Or     DateTime <DtTm> [1..1]  20
{Or       FromDateTime <FrDtTm> [1..1] DateTime 20
Or       ToDateTime <ToDtTm> [1..1] DateTime 20
Or       FromToDateTime <FrToDtTm> [1..1] ± 21
Or       EqualDateTime <EQDtTm> [1..1] DateTime 21
Or}       NotEqualDateTime <NEQDtTm> [1..1] DateTime 21
Or}     Date <Dt> [1..1]  21
{Or       FromDate <FrDt> [1..1] Date 21
Or       ToDate <ToDt> [1..1] Date 21
Or       FromToDate <FrToDt> [1..1] ± 22
Or       EqualDate <EQDt> [1..1] Date 22
Or}       NotEqualDate <NEQDt> [1..1] Date 22
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
admi.005.001.02 ReportQueryRequestV02
Target2-Securities - Administration - Maintenance 2023 -
2024
14 March 2024
```

