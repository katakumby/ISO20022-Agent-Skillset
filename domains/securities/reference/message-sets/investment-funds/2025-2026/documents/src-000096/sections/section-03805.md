---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.32 Person Identification", "66.1.32.7 IndividualPerson38", "66.1.32.7.21 GDPRData <GDPRData>", "66.1.32.7.21.1 ConsentType <CnsntTp>", "66.1.32.7.21.1.1 Code <Cd>"]
file_pages: [5094]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.32.7.21.1.1 Code <Cd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5094 to 5094.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5094

```text
Definition: Type of consent.
ConsentType <CnsntTp> contains one of the following GDPRDataConsent1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5094
Or}   Proprietary <Prtry> [1..1] ± 5094
66.1.32.7.21.1.1  Code <Cd>
Presence: [1..1]
Definition: Consent type expressed as a code.
Datatype: "GDPRDataConsent1Code" on page 5307
CodeName Name Definition
DP00 ConsentMarketing Consent to authorise the controller of
personal data processing to process
personal data for marketing purposes.
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
66.1.32.7.21.1.2  Proprietary <Prtry>
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
66.1.32.7.21.2  ConsentIndicator <CnsntInd>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5094 May 2026
```

