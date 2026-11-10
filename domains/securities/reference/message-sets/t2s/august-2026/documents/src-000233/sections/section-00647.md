---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: []
file_pages: [886]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# Continuation at file page 886

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 886 to 886.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 886

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           TaxIdentificationNumber <TaxIdNb> [0..1] Text 1736
           NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1736
           PostalAddress <PstlAdr> [1..5] ± C10 1736
           PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1737
           SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 1737
         PayingAgent <PngAgt> [0..1]  1738
           Name <Nm> [1..1] Text 1738
           Identification <Id> [0..1]  1739
{Or             AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1739
Or}             ProprietaryIdentification <PrtryId> [1..1] ± 1739
           Purpose <Purp> [0..1] Text 1739
           TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1740
           RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1740
           RegistrationDate <RegnDt> [0..1] Date 1740
           TaxIdentificationNumber <TaxIdNb> [0..1] Text 1740
           NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1740
           PostalAddress <PstlAdr> [1..5] ± C10 1740
           PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1741
           SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 1741
         Depository <Dpstry> [0..1]  1742
           Name <Nm> [1..1] Text 1742
           Identification <Id> [0..1]  1743
{Or             AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1743
Or}             ProprietaryIdentification <PrtryId> [1..1] ± 1743
           Purpose <Purp> [0..1] Text 1743
           TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1744
           RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1744
           RegistrationDate <RegnDt> [0..1] Date 1744
           TaxIdentificationNumber <TaxIdNb> [0..1] Text 1744
           NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1744
           PostalAddress <PstlAdr> [1..5] ± C10 1744
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 886 August 2026
```

