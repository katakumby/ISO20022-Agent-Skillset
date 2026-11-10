---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["31 reda.010.001.01 SecurityQueryV01", "31.4 Message Building Blocks", "31.4.2 RequestType <ReqTp>"]
file_pages: [1768, 1769]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.010.001.01"]
---

# 31.4.2 RequestType <ReqTp>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1768 to 1769.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1768

```text
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader1" on page 2982 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 2982
   CreationDateTime <CreDtTm> [0..1] DateTime 2982
31.4.2 RequestType <ReqTp>
Presence: [0..1]
Definition: Defines the type of action to be performed in the request.
RequestType <ReqTp> contains the following elements (see "GenericIdentification1" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2966
   SchemeName <SchmeNm> [0..1] Text 2966
   Issuer <Issr> [0..1] Text 2966
31.4.3 SearchCriteria <SchCrit>
Presence: [1..1]
Definition: Defines the criteria to be used to query the securities reference data by the executing
system.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.010.001.01 SecurityQueryV01
Target2-Securities 1768 August 2026
```

## File page 1769

```text
SearchCriteria <SchCrit> contains the following SecuritiesSearchCriteria4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentIdentification <FinInstrmId> [0..1] ± C4, C5,
C7, C8,
C9
1770
   ClassificationFinancialInstrument <ClssfctnFinInstrm> [0..1] IdentifierSet 1771
   MaturityDate <MtrtyDt> [0..1]  1771
{Or     FromDate <FrDt> [1..1] Date 1771
Or     ToDate <ToDt> [1..1] Date 1771
Or     FromToDate <FrToDt> [1..1] ± 1771
Or     EqualDate <EQDt> [1..1] Date 1772
Or}     NotEqualDate <NEQDt> [1..1] Date 1772
   IssueDate <IsseDt> [0..1]  1772
{Or     FromDate <FrDt> [1..1] Date 1772
Or     ToDate <ToDt> [1..1] Date 1772
Or     FromToDate <FrToDt> [1..1] ± 1773
Or     EqualDate <EQDt> [1..1] Date 1773
Or}     NotEqualDate <NEQDt> [1..1] Date 1773
   IssueCurrency <IsseCcy> [0..1] CodeSet C1 1773
   CountryOfIssue <CtryOfIsse> [0..1] CodeSet C3 1773
   SecurityStatus <SctySts> [0..1]  1774
{Or     Code <Cd> [1..1] CodeSet 1774
Or}     Proprietary <Prtry> [1..1] ± 1774
   MaintainingCSD <MntngCSD> [0..1]  1774
{Or     OrganisationIdentification <OrgId> [1..1] ± 1775
Or}     CombinedIdentification <CmbndId> [1..1] ± 1775
   InvestorCSD <InvstrCSD> [0..1]  1775
{Or     OrganisationIdentification <OrgId> [1..1] ± 1775
Or}     CombinedIdentification <CmbndId> [1..1] ± 1776
   IssuerCSD <IssrCSD> [0..1]  1776
{Or     OrganisationIdentification <OrgId> [1..1] ± 1776
Or}     CombinedIdentification <CmbndId> [1..1] ± 1776
   TechnicalIssuerCSD <TechIssrCSD> [0..1]  1777
{Or     OrganisationIdentification <OrgId> [1..1] ± 1777
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.010.001.01 SecurityQueryV01
Target2-Securities 1769 August 2026
```

