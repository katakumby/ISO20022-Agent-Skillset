---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["24 sese.001.001.10 TransferOutInstructionV10", "24.4 Message Building Blocks", "24.4.5 MasterReference <MstrRef>", "24.4.6.12 UnitsDetails <UnitsDtls>", "24.4.6.12.8 TransactionOverhead <TxOvrhd>", "24.4.6.12.8.7 DigitalNetworkFee <DgtlNtwkFee>", "24.4.6.12.8.7.1 FinancialInstrumentIdentification <FinInstrmId>", "24.4.6.12.8.7.1.1 ISIN <ISIN>"]
file_pages: [476]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.001.001.10"]
---

# 24.4.6.12.8.7.1.1 ISIN <ISIN>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 476 to 476.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 476

```text
24.4.6.12.8.7.1.1  ISIN <ISIN>
Presence: [0..1]
Definition: International Securities Identification Number (ISIN). A numbering system designed by the
United Nation's International Organisation for Standardisation (ISO). The ISIN is composed of a 2-
character prefix representing the country of issue, followed by the national security number (if one
exists), and a check digit. Each country has a national numbering agency that assigns ISIN numbers for
securities in that country.
Datatype: "ISINOct2015Identifier" on page 5395
24.4.6.12.8.7.1.2  OtherIdentification <OthrId>
Presence: [0..*]
Definition: Identification of a security by proprietary or domestic identification scheme.
OtherIdentification <OthrId> contains the following OtherIdentification8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 476
   Suffix <Sfx> [0..1] Text 476
   Type <Tp> [1..1]  476
{Or     Code <Cd> [1..1] CodeSet 477
Or}     Proprietary <Prtry> [1..1] Text 478
24.4.6.12.8.7.1.2.1  Identification <Id>
Presence: [1..1]
Definition: Identification of a security.
Datatype: "Max35Text" on page 5403
24.4.6.12.8.7.1.2.2  Suffix <Sfx>
Presence: [0..1]
Definition: Identifies the suffix of the security identification.
Datatype: "Max16Text" on page 5402
24.4.6.12.8.7.1.2.3  Type <Tp>
Presence: [1..1]
Definition: Type of the identification.
Type <Tp> contains one of the following IdentificationSource6Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 477
Or}   Proprietary <Prtry> [1..1] Text 478
Approved by the Securities SEG on 27 January 2026 sese.001.001.10 TransferOutInstructionV10
Investment Funds - Maintenance 2025 - 2026 476 May 2026
```

