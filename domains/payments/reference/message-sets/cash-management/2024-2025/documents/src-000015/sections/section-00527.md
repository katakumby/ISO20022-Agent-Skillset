---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["30 camt.069.001.05 GetStandingOrderV05", "30.4 Message Building Blocks"]
file_pages: [689, 690]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.069.001.05"]
---

# 30.4 Message Building Blocks

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 689 to 690.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 689

```text
C5 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C6 IdentificationAndProxyGuideline
If the account identification is not defined through a conventional identification such as an email
address or a mobile number, then the proxy element should be used for the identification of the
account.
C7 IdentificationOrProxyPresenceRule
Identification must be present or Proxy must be present. Both may be present.
C8 ReturnCriteriaAndOrSearchCriteriaRule
If ReturnCriteria is not present, then at least one occurrence of SearchCriteria must be present.
If ReturnCriteria is present, then any occurrence of SearchCriteria is optional.
C9 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
30.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
30.4.1 MessageHeader <MsgHdr>
Presence: [1..1]
Definition: Common business identification for the message.
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader4" on page 812 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 812
   CreationDateTime <CreDtTm> [0..1] DateTime 812
   RequestType <ReqTp> [0..1]  813
{Or     Code <Cd> [1..1] CodeSet 813
Or}     Proprietary <Prtry> [1..1] ± 813
30.4.2 StandingOrderQueryDefinition <StgOrdrQryDef>
Presence: [0..1]
Definition: Defines the account query criteria.
Approved by the Payments SEG on 04 February 2025 camt.069.001.05 GetStandingOrderV05
Cash Management - Maintenance 2024 - 2025 689 February 2025
```

## File page 690

```text
StandingOrderQueryDefinition <StgOrdrQryDef> contains the following StandingOrderQuery5
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   QueryType <QryTp> [0..1] CodeSet 691
   StandingOrderCriteria <StgOrdrCrit> [0..1]  691
{Or     QueryName <QryNm> [1..1] Text 693
Or}     NewCriteria <NewCrit> [1..1]  C8 693
       NewQueryName <NewQryNm> [0..1] Text 695
       SearchCriteria <SchCrit> [0..*]  695
         KeyAttributesIndicator <KeyAttrbtsInd> [0..1] Indicator 696
         StandingOrderIdentification <StgOrdrId> [0..1] Text 696
         Type <Tp> [0..1]  697
{Or           Code <Cd> [1..1] CodeSet 697
Or}           Proprietary <Prtry> [1..1] ± 697
         Account <Acct> [0..1] ± C7, C6 697
         Currency <Ccy> [0..1] CodeSet C1 698
         ValidityPeriod <VldtyPrd> [0..1]  698
{Or           FromDate <FrDt> [1..1] Date 699
Or           ToDate <ToDt> [1..1] Date 699
Or}           FromToDate <FrToDt> [1..1] ± 699
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
Approved by the Payments SEG on 04 February 2025 camt.069.001.05 GetStandingOrderV05
Cash Management - Maintenance 2024 - 2025 690 February 2025
```

