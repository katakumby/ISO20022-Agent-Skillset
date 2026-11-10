---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.11.19 DateDetails <DtDtls>", "3.4.11.19.10 BorrowerStockLendingDeadline <BrrwrStockLndgDdln>", "3.4.11.19.10.2 Borrower <Brrwr>"]
file_pages: [152]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.11.19.10.2 Borrower <Brrwr>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 152 to 152.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 152

```text
Definition: Date/time set as the deadline to respond, with instructions, to an outstanding event for which
the underlying security is out on loan.
StockLendingDeadline <StockLndgDdln> contains one of the following elements (see
"DateFormat43Choice" on page 843 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 843
Or}   DateCode <DtCd> [1..1]  844
{Or     Code <Cd> [1..1] CodeSet 844
Or}     Proprietary <Prtry> [1..1] ± 844
3.4.11.19.10.2  Borrower <Brrwr>
Presence: [1..1]
Definition: Party who has borrowed stocks on loan.
Borrower <Brrwr> contains one of the following elements (see "PartyIdentification127Choice" on
page 1037 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C1 1038
Or}   ProprietaryIdentification <PrtryId> [1..1] ± 1038
3.4.11.19.11  EndOfSecuritiesBlockingPeriod <EndOfSctiesBlckgPrd>
Presence: [0..1]
Definition: Date until which the blocking of securities can occur upon instructing this option.
EndOfSecuritiesBlockingPeriod <EndOfSctiesBlckgPrd> contains one of the following elements
(see "DateFormat59Choice" on page 847 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 847
Or}   DateCode <DtCd> [1..1]  847
{Or     Code <Cd> [1..1] CodeSet 847
Or}     Proprietary <Prtry> [1..1] ± 848
3.4.11.19.12  DocumentationDeadline <DcmnttnDdln>
Presence: [0..1]
Definition: Date/Time by when the documentation must be provided.
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 152 February 2026
```

