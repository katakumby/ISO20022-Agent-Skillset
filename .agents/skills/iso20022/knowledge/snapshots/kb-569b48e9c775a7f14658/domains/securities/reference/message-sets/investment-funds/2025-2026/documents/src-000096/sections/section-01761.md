---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "46.4 Message Building Blocks", "46.4.5 MultipleExecutionDetails <MltplExctnDtls>", "46.4.5.10 IndividualExecutionDetails <IndvExctnDtls>", "46.4.5.10.34 DigitalAssetSettlement <DgtlAsstSttlm>", "46.4.5.10.34.1 FinancialInstrumentIdentification <FinInstrmId>", "46.4.5.10.34.1.1 ISIN <ISIN>"]
file_pages: [2460]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.006.001.06"]
---

# 46.4.5.10.34.1.1 ISIN <ISIN>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2460 to 2460.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2460

```text
46.4.5.10.34.1.1  ISIN <ISIN>
Presence: [0..1]
Definition: International Securities Identification Number (ISIN). A numbering system designed by the
United Nation's International Organisation for Standardisation (ISO). The ISIN is composed of a 2-
character prefix representing the country of issue, followed by the national security number (if one
exists), and a check digit. Each country has a national numbering agency that assigns ISIN numbers for
securities in that country.
Datatype: "ISINOct2015Identifier" on page 5395
46.4.5.10.34.1.2  OtherIdentification <OthrId>
Presence: [0..*]
Definition: Identification of a security by proprietary or domestic identification scheme.
OtherIdentification <OthrId> contains the following OtherIdentification8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2460
   Suffix <Sfx> [0..1] Text 2460
   Type <Tp> [1..1]  2460
{Or     Code <Cd> [1..1] CodeSet 2461
Or}     Proprietary <Prtry> [1..1] Text 2462
46.4.5.10.34.1.2.1  Identification <Id>
Presence: [1..1]
Definition: Identification of a security.
Datatype: "Max35Text" on page 5403
46.4.5.10.34.1.2.2  Suffix <Sfx>
Presence: [0..1]
Definition: Identifies the suffix of the security identification.
Datatype: "Max16Text" on page 5402
46.4.5.10.34.1.2.3  Type <Tp>
Presence: [1..1]
Definition: Type of the identification.
Type <Tp> contains one of the following IdentificationSource6Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2461
Or}   Proprietary <Prtry> [1..1] Text 2462
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2460 May 2026
```

