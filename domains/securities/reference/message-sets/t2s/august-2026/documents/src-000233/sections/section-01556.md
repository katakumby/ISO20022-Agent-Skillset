---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["46 reda.026.001.01 EligibleCounterpartCSDCreationRequestV01", "46.2 Structure"]
file_pages: [2180]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.026.001.01"]
---

# 46.2 Structure

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2180 to 2180.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2180

```text
46.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <ElgblCntrptCSDCreReq> [1..1]  
   MessageHeader <MsgHdr> [0..1] ± 2181
   EligibleCounterpartCSD <ElgblCntrptCSD> [1..1]  2181
     IssuerIdentification <IssrId> [1..1]  2182
{Or       OrganisationIdentification <OrgId> [1..1] ± 2182
Or}       CombinedIdentification <CmbndId> [1..1] ± 2182
     EligibleCounterpartIdentification <ElgblCntrptId> [1..1]  2182
{Or       OrganisationIdentification <OrgId> [1..1] ± 2183
Or}       CombinedIdentification <CmbndId> [1..1] ± 2183
     ValidFrom <VldFr> [1..1] Date 2183
     ValidTo <VldTo> [0..1] Date 2183
     EligibilityType <ElgbltyTp> [1..1] CodeSet 2183
     EligibilityIdentification <ElgbltyId> [1..1]  2184
{Or       Country <Ctry> [1..1] CodeSet C2 2184
Or       FinancialInstrumentIdentification <FinInstrmId> [1..1] IdentifierSet 2184
Or}       IssuerCSDIdentification <IssrCSDId> [1..1]  2185
{Or         OrganisationIdentification <OrgId> [1..1] ± 2185
Or}         CombinedIdentification <CmbndId> [1..1] ± 2185
   SupplementaryData <SplmtryData> [0..*] ± C3 2185
46.3 Constraints
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.026.001.01
EligibleCounterpartCSDCreationRequestV01
Target2-Securities 2180 August 2026
```

