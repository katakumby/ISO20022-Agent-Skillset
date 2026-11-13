---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["30 camt.069.001.05 GetStandingOrderV05", "30.4 Message Building Blocks", "30.4.2 StandingOrderQueryDefinition <StgOrdrQryDef>", "30.4.2.1 QueryType <QryTp>"]
file_pages: [691, 692]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.069.001.05"]
---

# 30.4.2.1 QueryType <QryTp>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 691 to 692.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 691

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         DebtorAccountIndicator <DbtrAcctInd> [0..1] Indicator 703
         CreditorAccountIndicator <CdtrAcctInd> [0..1] Indicator 703
         AssociatedPoolAccount <AssoctdPoolAcct> [0..1] Indicator 703
         FrequencyIndicator <FrqcyInd> [0..1] Indicator 704
         ExecutionTypeIndicator <ExctnTpInd> [0..1] Indicator 704
         ValidityFromIndicator <VldtyFrInd> [0..1] Indicator 704
         ValidToIndicator <VldToInd> [0..1] Indicator 704
         LinkSetIdentificationIndicator <LkSetIdInd> [0..1] Indicator 704
         LinkSetOrderIdentificationIndicator
<LkSetOrdrIdInd>
[0..1] Indicator 704
         LinkSetOrderSequenceIndicator
<LkSetOrdrSeqInd>
[0..1] Indicator 705
         TotalAmountIndicator <TtlAmtInd> [0..1] Indicator 705
         ZeroSweepIndicator <ZeroSweepInd> [0..1] Indicator 705
30.4.2.1  QueryType <QryTp>
Presence: [0..1]
Definition: Specifies the type of matching items to be returned in the response to the query.
Datatype: "QueryType2Code" on page 872
CodeName Name Definition
ALLL All Specifies that the query requests that all
matching items be returned.
CHNG Changed Specifies that the query requests that
only new matching items since the last
similar query be returned.
MODF Modified Specifies that the query requests that
only items that have changed since the
last query be returned.
DELD Deleted Specifies that the query requests that
items that have been deleted since the
last query be returned.
30.4.2.2  StandingOrderCriteria <StgOrdrCrit>
Presence: [0..1]
Definition: Definition of the standing order query criteria.
Approved by the Payments SEG on 04 February 2025 camt.069.001.05 GetStandingOrderV05
Cash Management - Maintenance 2024 - 2025 691 February 2025
```

## File page 692

```text
StandingOrderCriteria <StgOrdrCrit> contains one of the following StandingOrderCriteria5Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   QueryName <QryNm> [1..1] Text 693
Or}   NewCriteria <NewCrit> [1..1]  C8 693
     NewQueryName <NewQryNm> [0..1] Text 695
     SearchCriteria <SchCrit> [0..*]  695
       KeyAttributesIndicator <KeyAttrbtsInd> [0..1] Indicator 696
       StandingOrderIdentification <StgOrdrId> [0..1] Text 696
       Type <Tp> [0..1]  697
{Or         Code <Cd> [1..1] CodeSet 697
Or}         Proprietary <Prtry> [1..1] ± 697
       Account <Acct> [0..1] ± C7, C6 697
       Currency <Ccy> [0..1] CodeSet C1 698
       ValidityPeriod <VldtyPrd> [0..1]  698
{Or         FromDate <FrDt> [1..1] Date 699
Or         ToDate <ToDt> [1..1] Date 699
Or}         FromToDate <FrToDt> [1..1] ± 699
       SystemMember <SysMmb> [0..1] ± 699
       ResponsibleParty <RspnsblPty> [0..1] ± 700
       AssociatedPoolAccount <AssoctdPoolAcct> [0..1] ± 701
       LinkSetIdentification <LkSetId> [0..1] Text 701
       LinkSetOrderIdentification <LkSetOrdrId> [0..1] Text 701
       LinkSetOrderSequence <LkSetOrdrSeq> [0..1] Quantity 701
       ZeroSweepIndicator <ZeroSweepInd> [0..1] Indicator 701
     ReturnCriteria <RtrCrit> [0..1]  701
       StandingOrderIdentificationIndicator
<StgOrdrIdInd>
[0..1] Indicator 702
       TypeIndicator <TpInd> [0..1] Indicator 702
       SystemMemberIndicator <SysMmbInd> [0..1] Indicator 702
       ResponsiblePartyIndicator <RspnsblPtyInd> [0..1] Indicator 703
       CurrencyIndicator <CcyInd> [0..1] Indicator 703
       DebtorAccountIndicator <DbtrAcctInd> [0..1] Indicator 703
       CreditorAccountIndicator <CdtrAcctInd> [0..1] Indicator 703
Approved by the Payments SEG on 04 February 2025 camt.069.001.05 GetStandingOrderV05
Cash Management - Maintenance 2024 - 2025 692 February 2025
```

