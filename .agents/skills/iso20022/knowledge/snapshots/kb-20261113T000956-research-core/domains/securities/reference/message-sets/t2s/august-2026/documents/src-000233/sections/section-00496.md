---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["27 reda.006.001.01 SecurityCreationRequestV01", "27.3 Constraints"]
file_pages: [635]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.006.001.01"]
topic_continuations: [{"constraint_ids": ["C6", "C7", "C8", "C9", "C10", "C11", "C12", "C13", "C14"], "until_heading": "27.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 636, "topic": "27.3 Constraints", "reference_path": "domains/securities/reference/message-sets/t2s/august-2026/documents/src-000233/sections/section-00497.md"}]
---

# 27.3 Constraints

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 635 to 635.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

The 27.3 Constraints topic continues in [Constraints continuation C6–C14 (file p636)](section-00497.md#file-page-636). Read the text before **27.4 Message Building Blocks** on that page to include the remaining conditions and qualifications. The file-page range above describes this file only.
<!-- PDF-TOPIC-NAV-END -->

## File page 635

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
{Or           AnyBIC <AnyBIC> [1..1] IdentifierSet C3 821
Or}           ProprietaryIdentification <PrtryId> [1..1] ± 821
         Purpose <Purp> [0..1] Text 821
         TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 822
         RegistrationCountry <RegnCtry> [0..1] CodeSet C4 822
         RegistrationDate <RegnDt> [0..1] Date 822
         TaxIdentificationNumber <TaxIdNb> [0..1] Text 822
         NationalRegistrationNumber <NtlRegnNb> [0..1] Text 822
         PostalAddress <PstlAdr> [1..5] ± C10 822
         PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 823
         SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 823
   SupplementaryData <SplmtryData> [0..*] ± C14 824
27.3 Constraints
C1 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
C2 ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the
Currency is exchanged.
C3 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C4 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C5 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 635 August 2026
```

