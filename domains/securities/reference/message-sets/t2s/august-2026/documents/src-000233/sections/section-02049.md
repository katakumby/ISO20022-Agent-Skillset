---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["81 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "81.4 Message Building Blocks", "81.4.6 Penalty <Pnlty>", "81.4.6.11 PenaltyPerCounterparty <PnltyPerCtrPty>", "81.4.6.11.4 PenaltyDetails <PnltyDtls>", "81.4.6.11.4.4 Status <Sts>", "81.4.6.11.4.4.2 Reason <Rsn>", "81.4.6.11.4.4.2.1 Reason <Rsn>", "81.4.6.11.4.4.2.1.2 Proprietary <Prtry>"]
file_pages: [2797]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.044.001.01"]
---

# 81.4.6.11.4.4.2.1.2 Proprietary <Prtry>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2797 to 2797.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2797

```text
CodeName Name Definition
components, a cyber-attack, network
problems.
SWIC Switched Penalty has been switched between the
failing and non-failing party.
SESU SettlementSuspended Penalty was removed becuase of ISIN
suspension from settlement due to a
reconciliation issue under Article 65 (2)
and (6) of the RTS on CSD
Requirements.
SEMP SettlementOnMultiplePlatforms Settlement on multiple platforms where
one of the platforms is closed for
settlement (either cash or securities).
RALO Reallocated Re-allocation of a late matching fail
penalty from the instructing party to the
delivering/receiving party.
OTHR Other See narrative.
NEWP NewPenalty Penalty is new.
INTS InternalisedSettlement Penalty is not computed because the
settlement has been internalised.
INSO Insolvency Penalty was removed becuase
insolvency proceedings are opened
against the failing participant.
CORP CorporateAction Specifies that due to a specific corporate
action, the security does no longer
exists.
NOSU NotSubject Penalty is not computed or removed
because the security is not subject to
penalties.
81.4.6.11.4.4.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Penalty status reason, in a proprietary form.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
81.4.6.11.4.4.2.2  AdditionalStatusReason <AddtlStsRsn>
Presence: [0..1]
Definition: Further details on the penalty status reason.
Datatype: "Max210Text" on page 3327
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities 2797 August 2026
```

