---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.3 Constraints"]
file_pages: [887]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
topic_continuations: [{"constraint_ids": ["C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "C13", "C14"], "until_heading": "28.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 888, "topic": "28.3 Constraints", "reference_path": "domains/securities/reference/message-sets/t2s/august-2026/documents/src-000233/sections/section-00649.md"}]
---

# 28.3 Constraints

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 887 to 887.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

The 28.3 Constraints topic continues in [Constraints continuation C3–C14 (file p888)](section-00649.md#file-page-888). Read the text before **28.4 Message Building Blocks** on that page to include the remaining conditions and qualifications. The file-page range above describes this file only.
<!-- PDF-TOPIC-NAV-END -->

## File page 887

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1745
           SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 1745
         UnderlyingRisk <UndrlygRsk> [0..1]  1746
           Name <Nm> [1..1] Text 1746
           Identification <Id> [0..1]  1747
{Or             AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1747
Or}             ProprietaryIdentification <PrtryId> [1..1] ± 1747
           Purpose <Purp> [0..1] Text 1747
           TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1748
           RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1748
           RegistrationDate <RegnDt> [0..1] Date 1748
           TaxIdentificationNumber <TaxIdNb> [0..1] Text 1748
           NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1748
           PostalAddress <PstlAdr> [1..5] ± C10 1748
           PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1749
           SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 1749
       SupplementaryData <SplmtryData> [0..*] ± C14 1750
   UpdateReason <UpdRsn> [0..1]  1750
{Or     Code <Cd> [1..1] CodeSet 1750
Or}     Proprietary <Prtry> [1..1] ± 1751
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C6, C7,
C8, C9,
C12
1751
   SupplementaryData <SplmtryData> [0..*] ± C14 1752
28.3 Constraints
C1 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
C2 ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 887 August 2026
```

