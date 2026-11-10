---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["30 camt.069.001.05 GetStandingOrderV05", "30.4 Message Building Blocks", "30.4.2 StandingOrderQueryDefinition <StgOrdrQryDef>", "30.4.2.2 StandingOrderCriteria <StgOrdrCrit>", "30.4.2.2.1 QueryName <QryNm>"]
file_pages: [693, 694]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.069.001.05"]
---

# 30.4.2.2.1 QueryName <QryNm>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 693 to 694.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 693

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
30.4.2.2.1  QueryName <QryNm>
Presence: [1..1]
Definition: Recalls the criteria (search and return criteria) defined in a preceding query.
Datatype: "Max35Text" on page 889
30.4.2.2.2  NewCriteria <NewCrit>
Presence: [1..1]
Definition: Explicitly defines the query criteria.
Impacted by: C8 "ReturnCriteriaAndOrSearchCriteriaRule"
Approved by the Payments SEG on 04 February 2025 camt.069.001.05 GetStandingOrderV05
Cash Management - Maintenance 2024 - 2025 693 February 2025
```

## File page 694

```text
NewCriteria <NewCrit> contains the following StandingOrderCriteria5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NewQueryName <NewQryNm> [0..1] Text 695
   SearchCriteria <SchCrit> [0..*]  695
     KeyAttributesIndicator <KeyAttrbtsInd> [0..1] Indicator 696
     StandingOrderIdentification <StgOrdrId> [0..1] Text 696
     Type <Tp> [0..1]  697
{Or       Code <Cd> [1..1] CodeSet 697
Or}       Proprietary <Prtry> [1..1] ± 697
     Account <Acct> [0..1] ± C7, C6 697
     Currency <Ccy> [0..1] CodeSet C1 698
     ValidityPeriod <VldtyPrd> [0..1]  698
{Or       FromDate <FrDt> [1..1] Date 699
Or       ToDate <ToDt> [1..1] Date 699
Or}       FromToDate <FrToDt> [1..1] ± 699
     SystemMember <SysMmb> [0..1] ± 699
     ResponsibleParty <RspnsblPty> [0..1] ± 700
     AssociatedPoolAccount <AssoctdPoolAcct> [0..1] ± 701
     LinkSetIdentification <LkSetId> [0..1] Text 701
     LinkSetOrderIdentification <LkSetOrdrId> [0..1] Text 701
     LinkSetOrderSequence <LkSetOrdrSeq> [0..1] Quantity 701
     ZeroSweepIndicator <ZeroSweepInd> [0..1] Indicator 701
   ReturnCriteria <RtrCrit> [0..1]  701
     StandingOrderIdentificationIndicator <StgOrdrIdInd> [0..1] Indicator 702
     TypeIndicator <TpInd> [0..1] Indicator 702
     SystemMemberIndicator <SysMmbInd> [0..1] Indicator 702
     ResponsiblePartyIndicator <RspnsblPtyInd> [0..1] Indicator 703
     CurrencyIndicator <CcyInd> [0..1] Indicator 703
     DebtorAccountIndicator <DbtrAcctInd> [0..1] Indicator 703
     CreditorAccountIndicator <CdtrAcctInd> [0..1] Indicator 703
     AssociatedPoolAccount <AssoctdPoolAcct> [0..1] Indicator 703
     FrequencyIndicator <FrqcyInd> [0..1] Indicator 704
     ExecutionTypeIndicator <ExctnTpInd> [0..1] Indicator 704
Approved by the Payments SEG on 04 February 2025 camt.069.001.05 GetStandingOrderV05
Cash Management - Maintenance 2024 - 2025 694 February 2025
```

