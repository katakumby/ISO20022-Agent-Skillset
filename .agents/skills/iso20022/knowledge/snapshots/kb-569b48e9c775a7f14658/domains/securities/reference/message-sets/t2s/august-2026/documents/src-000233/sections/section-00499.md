---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["27 reda.006.001.01 SecurityCreationRequestV01", "27.4 Message Building Blocks", "27.4.2 Security <Scty>", "27.4.2.1 FinancialInstrumentIdentification <FinInstrmId>"]
file_pages: [653]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.006.001.01"]
---

# 27.4.2.1 FinancialInstrumentIdentification <FinInstrmId>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 653 to 653.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 653

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}         ProprietaryIdentification <PrtryId> [1..1] ± 821
       Purpose <Purp> [0..1] Text 821
       TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 822
       RegistrationCountry <RegnCtry> [0..1] CodeSet C4 822
       RegistrationDate <RegnDt> [0..1] Date 822
       TaxIdentificationNumber <TaxIdNb> [0..1] Text 822
       NationalRegistrationNumber <NtlRegnNb> [0..1] Text 822
       PostalAddress <PstlAdr> [1..5] ± C10 822
       PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 823
       SecondaryCommunicationAddress
<ScndryComAdr>
[0..1] ± 823
27.4.2.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Identification of a security.
Impacted by: C6 "DescriptionPresenceRule", C7 "DescriptionUsageRule", C8 "ISINGuideline", C9
"ISINPresenceRule", C12 "OtherIdentificationPresenceRule"
FinancialInstrumentIdentification <FinInstrmId> contains the following elements (see
"SecurityIdentification39" on page 2945 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 2946
   OtherIdentification <OthrId> [0..*]  2947
     Identification <Id> [1..1] Text 2947
     Suffix <Sfx> [0..1] Text 2947
     Type <Tp> [1..1] ± 2947
   Description <Desc> [0..1] Text 2947
Constraints
• DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification must be
present.
On Condition
    /Description is absent
Following Must be True
    /ISIN Must be present
 Or    /OtherIdentification[*] Must be present
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 653 August 2026
```

