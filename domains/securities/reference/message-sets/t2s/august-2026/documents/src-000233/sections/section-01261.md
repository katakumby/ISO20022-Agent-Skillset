---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["31 reda.010.001.01 SecurityQueryV01", "31.4 Message Building Blocks", "31.4.4 SmallSetReturnCriteria <SmlSetRtrCrit>", "31.4.4.1 FinancialInstrumentIdentification <FinInstrmId>"]
file_pages: [1779]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.010.001.01"]
---

# 31.4.4.1 FinancialInstrumentIdentification <FinInstrmId>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1779 to 1779.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1779

```text
SmallSetReturnCriteria <SmlSetRtrCrit> contains the following SecuritiesReturnCriteria1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentIdentification <FinInstrmId> [1..1] Indicator 1779
   ISOSecurityLongName <ISOSctyLngNm> [1..1] Indicator 1779
   ISOSecurityShortName <ISOSctyShrtNm> [1..1] Indicator 1780
   ClassificationFinancialInstrument <ClssfctnFinInstrm> [1..1] Indicator 1780
   MaturityDate <MtrtyDt> [1..1] Indicator 1780
   IssueDate <IsseDt> [1..1] Indicator 1780
   IssueCurrency <IsseCcy> [1..1] Indicator 1780
   CountryOfIssue <CtryOfIsse> [1..1] Indicator 1780
   SecurityStatus <SctySts> [1..1] Indicator 1781
   InvestorCSD <InvstrCSD> [1..1] Indicator 1781
   IssuerCSD <IssrCSD> [1..1] Indicator 1781
   TechnicalIssuerCSD <TechIssrCSD> [1..1] Indicator 1781
   CSD <CSD> [1..1] Indicator 1781
   SecuritiesQuantityType <SctiesQtyTp> [1..1] Indicator 1782
   MinimumDenomination <MinDnmtn> [1..1] Indicator 1782
   MinimumMultipleQuantity <MinMltplQty> [1..1] Indicator 1782
   DeviatingSettlementUnit <DevtgSttlmUnit> [1..1] Indicator 1782
31.4.4.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Identification of a security.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 3323):
• Meaning When True: Requested
• Meaning When False: Not Requested
31.4.4.2  ISOSecurityLongName <ISOSctyLngNm>
Presence: [1..1]
Definition: Name of the security.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 3323):
• Meaning When True: Requested
• Meaning When False: Not Requested
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.010.001.01 SecurityQueryV01
Target2-Securities 1779 August 2026
```

