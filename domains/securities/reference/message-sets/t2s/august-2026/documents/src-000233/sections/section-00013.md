---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["2 admi.005.001.02 ReportQueryRequestV02", "2.4 Message Building Blocks", "2.4.2 ReportQueryCriteria <RptQryCrit>", "2.4.2.2 SearchCriteria <SchCrit>", "2.4.2.2.1 AccountIdentification <AcctId>", "2.4.2.2.1.1 Equal <EQ>"]
file_pages: [43, 44]
content_origin: "source-text-extraction"
mentioned_message_ids: ["admi.005.001.02"]
---

# 2.4.2.2.1.1 Equal <EQ>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 43 to 44.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 43

```text
2.4.2.2.1.1  Equal <EQ>
Presence: [1..1]
Definition: Search for one or more accounts based on exact identification of the account(s).
Equal <EQ> contains one of the following elements (see "AccountIdentification4Choice" on page 2836
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C2 2837
Or}   Other <Othr> [1..1] ± 2837
2.4.2.2.1.2  ContainText <CTTxt>
Presence: [1..1]
Definition: Search for one or more accounts based on partial identification of the account(s).
Datatype: "Max35Text" on page 3328
2.4.2.2.1.3  NotContainText <NCTTxt>
Presence: [1..1]
Definition: Search for one or more accounts based on a pattern that cannot be contained in the account
identification.
Datatype: "Max35Text" on page 3328
2.4.2.2.2  Balance <Bal>
Presence: [0..*]
Definition: Numerical representation of the net increases and decreases in an account at a specific
point in time. A cash balance is calculated from a sum of cash credits minus a sum of cash debits.
Impacted by: C3 "CounterpartyIdentification1Rule", C4 "CounterpartyIdentification2Rule"
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
admi.005.001.02 ReportQueryRequestV02
Target2-Securities 43 August 2026
```

## File page 44

```text
Balance <Bal> contains the following CashBalance14 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..*]  45
{Or     Code <Cd> [1..1] CodeSet 45
Or}     Proprietary <Prtry> [1..1] Text 45
   CounterpartyType <CtrPtyTp> [1..1] CodeSet 45
   CounterpartyIdentification <CtrPtyId> [0..*] ± 46
   ValueDate <ValDt> [0..*]  46
{Or     DateTime <DtTm> [1..1]  47
{Or       FromDateTime <FrDtTm> [1..1] DateTime 47
Or       ToDateTime <ToDtTm> [1..1] DateTime 47
Or       FromToDateTime <FrToDtTm> [1..1] ± 48
Or       EqualDateTime <EQDtTm> [1..1] DateTime 48
Or}       NotEqualDateTime <NEQDtTm> [1..1] DateTime 48
Or}     Date <Dt> [1..1]  48
{Or       FromDate <FrDt> [1..1] Date 48
Or       ToDate <ToDt> [1..1] Date 48
Or       FromToDate <FrToDt> [1..1] ± 49
Or       EqualDate <EQDt> [1..1] Date 49
Or}       NotEqualDate <NEQDt> [1..1] Date 49
   ProcessingDate <PrcgDt> [0..1]  49
{Or     DateTime <DtTm> [1..1]  50
{Or       FromDateTime <FrDtTm> [1..1] DateTime 50
Or       ToDateTime <ToDtTm> [1..1] DateTime 50
Or       FromToDateTime <FrToDtTm> [1..1] ± 51
Or       EqualDateTime <EQDtTm> [1..1] DateTime 51
Or}       NotEqualDateTime <NEQDtTm> [1..1] DateTime 51
Or}     Date <Dt> [1..1]  51
{Or       FromDate <FrDt> [1..1] Date 51
Or       ToDate <ToDt> [1..1] Date 51
Or       FromToDate <FrToDt> [1..1] ± 52
Or       EqualDate <EQDt> [1..1] Date 52
Or}       NotEqualDate <NEQDt> [1..1] Date 52
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
admi.005.001.02 ReportQueryRequestV02
Target2-Securities 44 August 2026
```

