---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.13 CorporateActionMovementDetails <CorpActnMvmntDtls>", "7.4.13.18 DateDetails <DtDtls>", "7.4.13.18.2 CoverExpirationDeadline <CoverXprtnDdln>"]
file_pages: [438]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.13.18.2 CoverExpirationDeadline <CoverXprtnDdln>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 438 to 438.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 438

```text
Definition: Date/time that the account servicer has set as the deadline to respond, with instructions, to
an outstanding event, giving the holder eligibility to incentives.
EarlyResponseDeadline <EarlyRspnDdln> contains one of the following elements (see
"DateFormat43Choice" on page 843 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 843
Or}   DateCode <DtCd> [1..1]  844
{Or     Code <Cd> [1..1] CodeSet 844
Or}     Proprietary <Prtry> [1..1] ± 844
7.4.13.18.2  CoverExpirationDeadline <CoverXprtnDdln>
Presence: [0..1]
Definition: Last day a holder can deliver the securities that it had elected on and/or previously protected.
CoverExpirationDeadline <CoverXprtnDdln> contains one of the following elements (see
"DateFormat43Choice" on page 843 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 843
Or}   DateCode <DtCd> [1..1]  844
{Or     Code <Cd> [1..1] CodeSet 844
Or}     Proprietary <Prtry> [1..1] ± 844
7.4.13.18.3  ProtectDeadline <PrtctDdln>
Presence: [0..1]
Definition: Last date/time a holder can request to defer delivery of securities pursuant to a notice of
guaranteed delivery or other required documentation.
ProtectDeadline <PrtctDdln> contains one of the following elements (see "DateFormat43Choice" on
page 843 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 843
Or}   DateCode <DtCd> [1..1]  844
{Or     Code <Cd> [1..1] CodeSet 844
Or}     Proprietary <Prtry> [1..1] ± 844
7.4.13.18.4  MarketDeadline <MktDdln>
Presence: [0..1]
Definition: Issuer or issuer's agent deadline to respond with an instruction to an outstanding offer or
privilege.
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 438 February 2026
```

