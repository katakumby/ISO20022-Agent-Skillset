---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["6 reda.010.001.01 SecurityQueryV01", "6.4 Message Building Blocks", "6.4.4 SmallSetReturnCriteria <SmlSetRtrCrit>", "6.4.4.1 FinancialInstrumentIdentification <FinInstrmId>"]
file_pages: [89]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.010.001.01"]
---

# 6.4.4.1 FinancialInstrumentIdentification <FinInstrmId>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 89 to 89.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 89

```text
SmallSetReturnCriteria <SmlSetRtrCrit> contains the following SecuritiesReturnCriteria1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentIdentification <FinInstrmId> [1..1] Indicator 89
   ISOSecurityLongName <ISOSctyLngNm> [1..1] Indicator 89
   ISOSecurityShortName <ISOSctyShrtNm> [1..1] Indicator 90
   ClassificationFinancialInstrument <ClssfctnFinInstrm> [1..1] Indicator 90
   MaturityDate <MtrtyDt> [1..1] Indicator 90
   IssueDate <IsseDt> [1..1] Indicator 90
   IssueCurrency <IsseCcy> [1..1] Indicator 90
   CountryOfIssue <CtryOfIsse> [1..1] Indicator 90
   SecurityStatus <SctySts> [1..1] Indicator 91
   InvestorCSD <InvstrCSD> [1..1] Indicator 91
   IssuerCSD <IssrCSD> [1..1] Indicator 91
   TechnicalIssuerCSD <TechIssrCSD> [1..1] Indicator 91
   CSD <CSD> [1..1] Indicator 91
   SecuritiesQuantityType <SctiesQtyTp> [1..1] Indicator 92
   MinimumDenomination <MinDnmtn> [1..1] Indicator 92
   MinimumMultipleQuantity <MinMltplQty> [1..1] Indicator 92
   DeviatingSettlementUnit <DevtgSttlmUnit> [1..1] Indicator 92
6.4.4.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Identification of a security.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 531):
• Meaning When True: Requested
• Meaning When False: Not Requested
6.4.4.2  ISOSecurityLongName <ISOSctyLngNm>
Presence: [1..1]
Definition: Name of the security.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 531):
• Meaning When True: Requested
• Meaning When False: Not Requested
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.010.001.01 SecurityQueryV01
Target2-Securities - Securities Reference Data 89 March 2024
```

