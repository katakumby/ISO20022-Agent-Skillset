---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.32 Person Identification", "66.1.32.3 IndividualPerson37", "66.1.32.3.21 GDPRData <GDPRData>", "66.1.32.3.21.1 ConsentType <CnsntTp>", "66.1.32.3.21.1.2 Proprietary <Prtry>"]
file_pages: [5074]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.32.3.21.1.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5074 to 5074.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5074

```text
CodeName Name Definition
DP03 ConsentProfilingTargeted Consent to authorise the controller of
personal data processing to process
personal data for profiling purposes in
order to formulate customised and
targeted product and service offers.
DP01 ConsentTransferSameMarketing Consent to authorise the controller of
personal data processing to transfer
personal data to other companies
belonging to the same group for
independent processing for marketing
purposes.
DP02 ConsentTransferThirdPartyMarketing Consent to authorise the controller of
personal data processing to transfer
personal data to third party companies
for independent processing for marketing
purposes.
66.1.32.3.21.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Consent type expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.32.3.21.2  ConsentIndicator <CnsntInd>
Presence: [1..1]
Definition: Indicates whether consent has been given.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.32.3.21.3  ConsentDate <CnsntDt>
Presence: [1..1]
Definition: Date of the consent.
Datatype: "ISODate" on page 5388
66.1.32.4  IndividualPerson30
Definition: Human entity, as distinguished from a corporate entity (which is sometimes referred to as an
'artificial person').
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5074 May 2026
```

