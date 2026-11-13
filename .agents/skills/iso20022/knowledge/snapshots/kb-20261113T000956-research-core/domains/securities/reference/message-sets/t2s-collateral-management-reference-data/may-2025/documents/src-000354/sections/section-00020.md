---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralManagementReferenceData"
source_ids: ["src-000354"]
source_editions: ["may-2025"]
message_ids: []
heading_path: ["4 reda.026.001.01 EligibleCounterpartCSDCreationRequestV01", "4.2 Structure"]
file_pages: [23]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.026.001.01"]
---

# 4.2 Structure

Source: [src-000354](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralManagementReferenceData_v1.pdf`. Locator: one-based file pages 23 to 23.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 23

```text
4.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <ElgblCntrptCSDCreReq> [1..1]  
   MessageHeader <MsgHdr> [0..1] ± 24
   EligibleCounterpartCSD <ElgblCntrptCSD> [1..1]  24
     IssuerIdentification <IssrId> [1..1]  25
{Or       OrganisationIdentification <OrgId> [1..1] ± 25
Or}       CombinedIdentification <CmbndId> [1..1] ± 25
     EligibleCounterpartIdentification <ElgblCntrptId> [1..1]  25
{Or       OrganisationIdentification <OrgId> [1..1] ± 26
Or}       CombinedIdentification <CmbndId> [1..1] ± 26
     ValidFrom <VldFr> [1..1] Date 26
     ValidTo <VldTo> [0..1] Date 26
     EligibilityType <ElgbltyTp> [1..1] CodeSet 26
     EligibilityIdentification <ElgbltyId> [1..1]  27
{Or       Country <Ctry> [1..1] CodeSet C2 27
Or       FinancialInstrumentIdentification <FinInstrmId> [1..1] IdentifierSet 27
Or}       IssuerCSDIdentification <IssrCSDId> [1..1]  28
{Or         OrganisationIdentification <OrgId> [1..1] ± 28
Or}         CombinedIdentification <CmbndId> [1..1] ± 28
   SupplementaryData <SplmtryData> [0..*] ± C3 28
4.3 Constraints
C1 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C2 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C3 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities SEG on 17 April 2025. reda.026.001.01
EligibleCounterpartCSDCreationRequestV01
Target2-Securities - Collateral Management Reference Data 23 May 2025
```

