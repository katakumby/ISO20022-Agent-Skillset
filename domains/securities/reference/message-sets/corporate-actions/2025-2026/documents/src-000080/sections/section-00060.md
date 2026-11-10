---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.10 CorporateActionDetails <CorpActnDtls>", "3.4.10.1 DateDetails <DtDtls>", "3.4.10.1.25 GuaranteedParticipationDate <GrntedPrtcptnDt>"]
file_pages: [106]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.10.1.25 GuaranteedParticipationDate <GrntedPrtcptnDt>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 106 to 106.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 106

```text
being traded cum or ex respectively, for example, a transaction dealt 'special' after the ex date would
result in the buyer being eligible for the entitlement. This is typically used in the UK and Irish markets.
SpecialExDate <SpclExDt> contains one of the following elements (see "DateFormat30Choice" on
page 842 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 842
Or}   DateCode <DtCd> [1..1]  842
{Or     Code <Cd> [1..1] CodeSet 843
Or}     Proprietary <Prtry> [1..1] ± 843
3.4.10.1.25  GuaranteedParticipationDate <GrntedPrtcptnDt>
Presence: [0..1]
Definition: Last date/time by which a buying counterparty to a trade can be sure that it will have the right
to participate in an event.
GuaranteedParticipationDate <GrntedPrtcptnDt> contains one of the following elements (see
"DateFormat30Choice" on page 842 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 842
Or}   DateCode <DtCd> [1..1]  842
{Or     Code <Cd> [1..1] CodeSet 843
Or}     Proprietary <Prtry> [1..1] ± 843
3.4.10.1.26  ElectionToCounterpartyMarketDeadline <ElctnToCtrPtyMktDdln>
Presence: [0..1]
Definition: Deadline by which an entitled holder needs to advise their counterparty to a transaction of
their election for a corporate action event, also known as Buyer Protection Deadline.
ElectionToCounterpartyMarketDeadline <ElctnToCtrPtyMktDdln> contains one of the following
elements (see "DateFormat43Choice" on page 843 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 843
Or}   DateCode <DtCd> [1..1]  844
{Or     Code <Cd> [1..1] CodeSet 844
Or}     Proprietary <Prtry> [1..1] ± 844
3.4.10.1.27  ElectionToCounterpartyResponseDeadline <ElctnToCtrPtyRspnDdln>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 106 February 2026
```

