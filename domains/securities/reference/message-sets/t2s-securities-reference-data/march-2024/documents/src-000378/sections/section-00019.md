---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["3 reda.007.001.01 SecurityMaintenanceRequestV01", "3.4 Message Building Blocks", "3.4.2 UpdateType <UpdTp>", "3.4.2.1 UpdateType <UpdTp>", "3.4.2.1.2 Delete <Del>", "3.4.2.1.2.3 SupplementaryData <SplmtryData>"]
file_pages: [44]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 3.4.2.1.2.3 SupplementaryData <SplmtryData>

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 44 to 44.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 44

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     PostalAddress <PstlAdr> [1..5] ± C10 316
     PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 317
     SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 317
   UnderlyingRisk <UndrlygRsk> [0..1]  318
     Name <Nm> [1..1] Text 318
     Identification <Id> [0..1]  319
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C3 319
Or}       ProprietaryIdentification <PrtryId> [1..1] ± 319
     Purpose <Purp> [0..1] Text 319
     TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 320
     RegistrationCountry <RegnCtry> [0..1] CodeSet C4 320
     RegistrationDate <RegnDt> [0..1] Date 320
     TaxIdentificationNumber <TaxIdNb> [0..1] Text 320
     NationalRegistrationNumber <NtlRegnNb> [0..1] Text 320
     PostalAddress <PstlAdr> [1..5] ± C10 320
     PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 321
     SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 321
3.4.2.1.2.3  SupplementaryData <SplmtryData>
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
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities - Securities Reference Data 44 March 2024
```

