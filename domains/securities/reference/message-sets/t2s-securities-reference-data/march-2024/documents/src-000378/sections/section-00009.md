---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["2 reda.006.001.01 SecurityCreationRequestV01", "2.4 Message Building Blocks", "2.4.3 SupplementaryData <SplmtryData>"]
file_pages: [20]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.006.001.01"]
---

# 2.4.3 SupplementaryData <SplmtryData>

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 20 to 20.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 20

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   UnderlyingRisk <UndrlygRsk> [0..1]  470
     Name <Nm> [1..1] Text 470
     Identification <Id> [0..1]  471
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C3 471
Or}       ProprietaryIdentification <PrtryId> [1..1] ± 471
     Purpose <Purp> [0..1] Text 471
     TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 472
     RegistrationCountry <RegnCtry> [0..1] CodeSet C4 472
     RegistrationDate <RegnDt> [0..1] Date 472
     TaxIdentificationNumber <TaxIdNb> [0..1] Text 472
     NationalRegistrationNumber <NtlRegnNb> [0..1] Text 472
     PostalAddress <PstlAdr> [1..5] ± C10 472
     PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 473
     SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 473
2.4.3 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C14 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 486 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 486
   Envelope <Envlp> [1..1] (External Schema) 486
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities - Securities Reference Data 20 March 2024
```

